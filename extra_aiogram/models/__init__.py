import importlib

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from extra_aiogram.config import settings
from .users import User
from .chats import Chat
from .groups import Group
from .groups_info import GroupInfo
from .messages import Message

metadata = MetaData()

# Создание движка SQLAlchemy, подключенного к базе данных
engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)

model_registry = []


# функция для регистрации моделей
def register_model(model_class):
    if model_class not in model_registry:
        model_registry.append(model_class)
        model_class.__table__.tometadata(metadata)


for class_name in settings.DEFAULT_MODELS:
    settings_module = importlib.import_module('extra_aiogram.models')
    model = getattr(settings_module, class_name)
    register_model(model)


# Функция для создания всех таблиц
def create_tables():
    metadata.create_all(engine)


# Функция для удаления всех таблиц (используйте с осторожностью!)
def drop_tables():
    metadata.drop_all(engine)
