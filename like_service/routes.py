from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import service

router = APIRouter(
    prefix="/like_service",
    tags=["like_service"],
)

@router.post("/messages/{message_id}/like")
def like_message(message_id: int, user_id: int, db: Session = Depends(get_db)):
    liked_message = service.like_message(db, user_id, message_id)

    if liked_message is None:
        raise HTTPException(status_code=400, detail="Message already liked or does not exist")
    
    return {"message": "Message liked successfully"}

@router.get("/messages/{message_id}/likes/count")
def get_like_count(message_id: int, db: Session = Depends(get_db)):
    like_count = service.get_like_count(db, message_id)
    if like_count is None:
        raise HTTPException(status_code=404, detail="Message not found or no likes")
    
    return {"like_count": like_count}