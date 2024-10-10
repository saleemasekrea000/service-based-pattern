from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import service, models
from dependencies import get_db

router = APIRouter(
    prefix="/user_service",
    tags=["user_service"],
)


@router.post("/users/")
def create_user(username: str, db: Session = Depends(get_db)):
    existing_user = service.get_user_by_username(db, username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return service.create_user(db=db, username=username)


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    # print("i recived user _id ",user_id)
    user = service.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user