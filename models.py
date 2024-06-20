from sqlalchemy import Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'))
    group: Mapped['Group'] = relationship('Group', back_populates='students')
    grades: Mapped[list['Grade']] = relationship('Grade', back_populates='student', overlaps="students")

class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    students: Mapped[list['Student']] = relationship('Student', back_populates='group')

class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    subjects_taught: Mapped[list['Subject']] = relationship('Subject', back_populates='teacher')

class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'))
    teacher: Mapped['Teacher'] = relationship('Teacher', back_populates='subjects_taught')
    students: Mapped[list['Student']] = relationship('Student', secondary='grades', overlaps="grades,student")

class Grade(Base):
    __tablename__ = 'grades'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'))
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    date_received: Mapped[Date] = mapped_column(Date)
    student: Mapped['Student'] = relationship('Student', back_populates='grades', overlaps="students,subject")
    subject: Mapped['Subject'] = relationship('Subject', overlaps="students")


# CLI TABLE
class Person(Base):
    __tablename__ = "person"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}')>"

