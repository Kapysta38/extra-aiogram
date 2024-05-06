import importlib

from sqlalchemy.ext.declarative import declarative_base

from extra_aiogram.config import settings

# Динамическая загрузка настраиваемого Base, если предоставлено
if settings.CUSTOM_BASE_MODULE:
    module_path, _, class_name = settings.CUSTOM_BASE_MODULE.rpartition('.')
    custom_module = importlib.import_module(module_path)
    Base = getattr(custom_module, class_name)
else:
    Base = declarative_base()
