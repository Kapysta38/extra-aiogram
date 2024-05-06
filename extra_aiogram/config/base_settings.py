from os import getenv


def get_boolean_env_var(env_var_name, default=False):
    value = getenv(env_var_name, str(default)).strip().lower()
    return value in ['true', '1', 't', 'y', 'yes']


def get_list_env_var(env_var_name, default="", separator=','):
    value = getenv(env_var_name, default)
    return [item.strip() for item in value.split(separator) if item.strip()]


class BaseSettings:

    def __init__(self):
        raise NotImplementedError("You must define settings parameters.")

    @property
    def DATABASE_URL(self):
        raise NotImplementedError("You must provide a DATABASE_URL.")

    @property
    def BOT_TOKEN(self):
        raise NotImplementedError("You must provide a BOT_TOKEN.")


class DefaultSettings(BaseSettings):
    def __init__(self):
        self.CUSTOM_BASE_MODULE = getenv('CUSTOM_BASE_MODULE')
        self.DEBUG = get_boolean_env_var('DEBUG')
        self.DEFAULT_MODELS = get_list_env_var('DEFAULT_MODELS', 'Chat, User, Message, GroupInfo, Group')

    @property
    def DATABASE_URL(self):
        return getenv("DATABASE_URL", 'sqlite:///default.db')

    @property
    def BOT_TOKEN(self):
        return getenv("BOT_TOKEN")
