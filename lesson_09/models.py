from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Subject(Base):
    __tablename__ = "subject"
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String(80))
    users = relationship("User", back_populates="subject")


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    user_email = Column(String(120))
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))
    subject = relationship("Subject", back_populates="users")
    student = relationship("Student", back_populates="user", uselist=False)
    group_students = relationship("GroupStudent", back_populates="user")


class Student(Base):
    __tablename__ = "student"
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    level = Column(String(60))
    education_form = Column(String(60))
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))

    user = relationship("User", back_populates="student")
    subject = relationship("Subject")


class GroupStudent(Base):
    __tablename__ = "group_student"
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    group_id = Column(Integer, primary_key=True)
    user = relationship("User", back_populates="group_students")


class Teacher(Base):
    __tablename__ = "teacher"
    teacher_id = Column(Integer, primary_key=True)
    email = Column(String(120))
    group_id = Column(Integer)
