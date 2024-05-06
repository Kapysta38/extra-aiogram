from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from extra_aiogram.config import settings
from .base import Base
from .users import User
from .chats import Chat
from .groups import Group
from .groups_info import GroupInfo
from .messages import Message

# Создание движка SQLAlchemy, подключенного к базе данных
engine = create_engine(settings.DATABASE_URL)  # Измените URL на вашу базу данных
Session = sessionmaker(bind=engine)


# Функция для создания всех таблиц
def create_tables():
    Base.metadata.create_all(engine)


# Функция для удаления всех таблиц (используйте с осторожностью!)
def drop_tables():
    Base.metadata.drop_all(engine)
