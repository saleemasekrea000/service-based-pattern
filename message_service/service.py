import models
import requests
from sqlalchemy.orm import Session

LIKE_SERVICE_URL = "http://like_service:8002/like_service/messages"

USER_SERVICE_URL = "http://user_service:8000/user_service/users"

def create_message(db: Session, content: str, creator_id: int):
    response = requests.get(f"{USER_SERVICE_URL}/{creator_id}")
    if response.status_code != 200:
        return "User Not found"
    
    message = models.Message(content=content, creator_id=creator_id)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_messages(db: Session, skip: int = 0, limit: int = 10):
    messages = db.query(models.Message).order_by(models.Message.id.desc()).offset(skip).limit(limit).all()
    
    for message in messages:
        message.like_count = get_like_count(message.id)
    
    return messages

def get_message(db: Session, message_id: int):
    message = db.query(models.Message).filter(models.Message.id == message_id).first()
    if message:
        message.like_count = get_like_count(message_id)
    return message

def get_like_count(message_id: int):
    try:
        response = requests.get(f"{LIKE_SERVICE_URL}/{message_id}/likes/count")
        if response.status_code == 200:
            return response.json().get('like_count', 0)
    except requests.RequestException:
        return 0
    return 0
