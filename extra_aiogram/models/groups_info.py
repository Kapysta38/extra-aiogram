from sqlalchemy import Column, Integer, String

from .base import Base


class GroupInfo(Base):
    __tablename__ = 'groups_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
