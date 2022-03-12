from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from dependencies import get_db
from sql_app import crud, models, schemas
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/lessons"
)


@router.get("/", response_model=List[schemas.Lesson])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_lessons(db, skip=skip, limit=limit)
    return items
