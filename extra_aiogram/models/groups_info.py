from sqlalchemy import Column, Integer, ForeignKey
from base import Base


class Group(Base):
    __tablename__ = 'groups'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups_info.id'), primary_key=True)
