from conf.db import session
from models import *
from sqlalchemy.exc import SQLAlchemyError
from faker import Faker
from random import choice, randint

fake = Faker()

NUM_STUDENTS = 30
NUM_GROUPS = 3
NUM_SUBJECTS = 8
NUM_TEACHERS = 5
GRADES_PER_STUDENT = 20

def insert_data():

    try:
        with session.begin():
            groups = [Group(name=fake.word()) for _ in range(NUM_GROUPS)]
            session.add_all(groups)

            students = []
            for _ in range(NUM_STUDENTS):
                student = Student(name=fake.name(), group=choice(groups))
                students.append(student)
            session.add_all(students)

            teachers = [Teacher(name=fake.name()) for _ in range(NUM_TEACHERS)]
            session.add_all(teachers)

            subjects = []
            for _ in range(NUM_SUBJECTS):
                subject = Subject(name=fake.word(), teacher=choice(teachers))
                subjects.append(subject)
            session.add_all(subjects)

            grades = []
            for student in students:
                for _ in range(GRADES_PER_STUDENT):
                    grade = Grade(
                        student=student,
                        subject=choice(subjects),
                        grade=randint(50, 100),
                        date_received=fake.date_between(start_date='-1y', end_date='today')
                    )
                    grades.append(grade)
            session.add_all(grades)
    except SQLAlchemyError as error:
        print(f"An error occurred: {error}")
        session.rollback()


insert_data()