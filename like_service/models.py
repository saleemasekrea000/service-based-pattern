from sqlalchemy import Column, Integer, DateTime
from database import Base

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    message_id = Column(Integer)
    like_at = Column(DateTime)
