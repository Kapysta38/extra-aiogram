import os
import importlib

from dotenv import load_dotenv

from .base_settings import DefaultSettings, BaseSettings

load_dotenv()


# Получение пути к пользовательскому классу настроек из переменной окружения
CUSTOM_SETTINGS_CLASS = os.getenv('CUSTOM_SETTINGS_CLASS')
if CUSTOM_SETTINGS_CLASS:

    module_path, _, class_name = CUSTOM_SETTINGS_CLASS.rpartition('.')
    settings_module = importlib.import_module(module_path)
    CustomSettings = getattr(settings_module, class_name)

    # Проверка, соответствует ли пользовательский класс настроек требованиям
    if not issubclass(CustomSettings, BaseSettings):
        raise TypeError("Custom settings class must inherit from BaseSettings.")

    settings = CustomSettings()
else:
    settings = DefaultSettings()
