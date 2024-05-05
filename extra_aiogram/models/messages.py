from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('chats.id'))
    text = Column(String(4096))
    media = Column(String(255))  # Путь к медиафайлу или URL
