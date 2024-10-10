from sqlalchemy.orm import Session
from models import Like
import requests

MESSAGE_SERVICE_URL = "http://message_service:8001/message_service" 
USER_SERVICE_URL = "http://user_service:8000/user_service/users"

def message_exists(message_id: int) -> bool:
    try:
        response = requests.get(f"{MESSAGE_SERVICE_URL}/{message_id}")
        if response.status_code == 200:
            return True
        else :
            return False
    except requests.RequestException:
        return False 

def user_exist(user_id:int) -> bool:
     try:
        response = requests.get(f"{USER_SERVICE_URL}/{user_id}")
        if response.status_code == 200:
            return True
     except requests.RequestException:
        return False

def like_message(db: Session, user_id: int, message_id: int):
    if not message_exists(message_id):
        return None

    existing_like = db.query(Like).filter(Like.user_id == user_id, Like.message_id == message_id).first()
    if existing_like:
        return None  

    new_like = Like(user_id=user_id, message_id=message_id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)

    return new_like

def get_like_count(db: Session, message_id: int) -> int:
    return db.query(Like).filter(Like.message_id == message_id).count()