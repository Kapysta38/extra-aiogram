from sqlalchemy import Column, Integer, String, Boolean, Date

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    bio = Column(String(140))
    first_name = Column(String(64))
    last_name = Column(String(64))
    is_bot = Column(Boolean, default=False)
    language_code = Column(String(10))
    is_premium = Column(Boolean, default=False)
    birthdate = Column(Date)
