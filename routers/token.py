from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from dependencies import get_db
from sql_app import crud, schemas

router = APIRouter(
    prefix="/users"
)


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_password = form_data.password + 'notreallyhashed'
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.email, "token_type": "bearer"}
