from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .users import User
from .base import Base  # Импорт Base из текущего пакета

# Создание движка SQLAlchemy, подключенного к базе данных
engine = create_engine('sqlite:///mydatabase.db')  # Измените URL на вашу базу данных
Session = sessionmaker(bind=engine)


# Функция для создания всех таблиц
def create_tables():
    Base.metadata.create_all(engine)


# Функция для удаления всех таблиц (используйте с осторожностью!)
def drop_tables():
    Base.metadata.drop_all(engine)
