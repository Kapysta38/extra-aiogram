from sqlalchemy import Column, Integer, String

from .base import Base


class Chat(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
