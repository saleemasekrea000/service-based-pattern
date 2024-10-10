from sqlalchemy import Column, Integer, String
from database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer,nullable=True)
    content = Column(String(400))