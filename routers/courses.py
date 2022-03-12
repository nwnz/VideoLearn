from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from dependencies import get_db
from sql_app import crud, models, schemas
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/courses"
)


@router.get("/", response_model=List[schemas.Course])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_courses(db, skip=skip, limit=limit)
    return items


@router.post("/{course_id}/lessons/", response_model=schemas.Lesson)
def create_lesson_for_course(course_id: int, item: schemas.LessonCreate, db: Session = Depends(get_db)):
    return crud.create_course_lesson(db=db, item=item, course_id=course_id)
