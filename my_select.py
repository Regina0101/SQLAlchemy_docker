from conf.db import session
from models import *
from sqlalchemy import func, desc


def select_1():
    return session.query(
        Student.name, func.avg(Grade.grade).label('average_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()


def select_2(subject_id):
    return session.query(
        Student.name, func.avg(Grade.grade).label('average_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc('average_grade')).first()


def select_3(subject_id):
    return session.query(
        Group.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Student, Group.id == Student.group_id
    ).join(Grade, Student.id == Grade.student_id
    ).filter(Grade.subject_id == subject_id
    ).group_by(Group.id
    ).all()

def select_4():
    return session.query(func.avg(Grade.grade)).scalar()

def select_5(teacher_id):
    return session.query(
        Subject.name
    ).filter(Subject.teacher_id == teacher_id).all()

def select_6(group_id):
    return session.query(
        Student.name
    ).filter(Student.group_id == group_id).all()

def select_7(subject_id, group_id):
    return session.query(
        Student.name, Grade.grade
    ).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

def select_8(teacher_id):
    return session.query(
        func.avg(Grade.grade).label('average_grade')
    ).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()

def select_9(student_id):
    return session.query(
        Subject.name
    ).join(Grade).filter(Grade.student_id == student_id).group_by(Subject.name).all()

def select_10(student_id, teacher_id):
    return (session.query(
        Subject.name
    ).join(Grade).join(Teacher).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
    .group_by(Subject.name)
    .all())


def select_11(student_id, teacher_id):
    return session.query(func.avg(Grade.grade)
    ).join(Subject).filter(Grade.student_id == student_id).filter(Subject.teacher_id == teacher_id).scalar()

def select_12(group_id,subject_id):
    return session.query(Student.name, Grade.grade
    ).join(Group, Group.id == Student.group_id
    ).join(Grade, Grade.student_id == Student.id
    ).join(Subject, Subject.id == Grade.subject_id
    ).filter(Group.id == group_id
    ).filter(Subject.id == subject_id
    ).order_by(Grade.date_received.desc()).first()


select1 = select_12(group_id=1, subject_id=1)

print(select1)