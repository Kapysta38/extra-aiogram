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

engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)

model_registry = []


# функция для регистрации моделей
def register_model(model_class):
    """
    Функция для регистрации моделей
    :param model_class:
    :return:
    """
    if model_class not in model_registry:
        model_registry.append(model_class)
        model_class.__table__.tometadata(metadata)


# Регистрируем стандартные модели
for class_name in settings.DEFAULT_MODELS:
    settings_module = importlib.import_module('extra_aiogram.models')
    model = getattr(settings_module, class_name)
    register_model(model)


def create_tables():
    """
    Создает таблицы, соответствующие зарегистрированным моделям.
    """
    metadata.create_all(engine)


def drop_tables():
    """
    Удаляет все таблицы в базе данных.
    """
    metadata.drop_all(engine)


def initialize_default_groups():
    """
    Инициализирует стандартные группы.

    Создает записи о стандартных группах в базе данных.
    """
    session = Session()
    session.add_all([
        GroupInfo(name='admin'),
        GroupInfo(name='user')
    ])
    session.commit()
