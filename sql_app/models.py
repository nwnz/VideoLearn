from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    courses = relationship("Course", back_populates="teacher")


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey("user.id"))

    teacher = relationship("User", back_populates="courses")
    lessons = relationship("Lesson", back_populates="course")


class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    course_id = Column(Integer, ForeignKey("course.id"))

    course = relationship("Course", back_populates="lessons")
