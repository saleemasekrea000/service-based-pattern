from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import service
from dependencies import get_db


router = APIRouter(
     prefix="/message_service",
     tags=["message_service"],
)


@router.post("/messages/")
def create_message(content: str, user_id: int, db: Session = Depends(get_db)):
    return service.create_message(db=db, content=content, creator_id=user_id)

@router.get("/messages/")
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = service.get_messages(db, skip=skip, limit=limit)
    return [{"id": msg.id, "content": msg.content, "creator_id": msg.creator_id, "like_count": msg.like_count} for msg in messages]


@router.get("/{message_id}")
def read_message(message_id: int, db: Session = Depends(get_db)):
    message = service.get_message(db, message_id)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return message