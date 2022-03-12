from pydantic import BaseModel


class LessonBase(BaseModel):
    title: str
    description: str | None = None


class LessonCreate(LessonBase):
    pass


class Lesson(LessonBase):
    id: int

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    title: str
    description: str | None = None


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    lessons: list[Lesson] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    courses: list[Course] = []

    class Config:
        orm_mode = True
