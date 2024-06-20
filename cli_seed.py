import argparse
from conf.db import session
from models import Person

def create_person(name):
    person = Person(name=name)
    session.add(person)
    session.commit()
    print(f"Added person: {person}")
    session.close()

def list_persons():
    persons = session.query(Person).all()
    session.close()
    print("List of people:")
    for person in persons:
        print(person)

def update_person(id, name):
    person = session.query(Person).filter_by(id=id).first()
    if person:
        person.name = name
        session.commit()
        print(f"Updated ID={id}: new name - {name}")
    else:
        print(f"Person ID={id} not found.")
    session.close()

def remove_person(id):
    person = session.query(Person).filter_by(id=id).first()
    if person:
        session.delete(person)
        session.commit()
        print(f"Deleted ID={id}")
    else:
        print(f"Person ID={id} not found.")
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', choices=['create', 'list', 'update', 'remove'], help='Action')
    parser.add_argument('-m', '--model', choices=['Person'], help='Model')
    parser.add_argument('--id', type=int, help='ID')
    parser.add_argument('-n', '--name', help='Name')

    args = parser.parse_args()

    if args.action == 'create' and args.model == 'Person' and args.name:
        create_person(name=args.name)
    elif args.action == 'list' and args.model == 'Person':
        list_persons()
    elif args.action == 'update' and args.model == 'Person' and args.id and args.name:
        update_person(id=args.id, name=args.name)
    elif args.action == 'remove' and args.model == 'Person' and args.id:
        remove_person(id=args.id)
    else:
        print("Error wrong args")
