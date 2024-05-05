from os import getenv


class BaseSettings:
    @property
    def DATABASE_URL(self):
        raise NotImplementedError("You must provide a DATABASE_URL.")

    @property
    def BOT_TOKEN(self):
        raise NotImplementedError("You must provide a BOT_TOKEN.")


class DefaultSettings(BaseSettings):
    CUSTOM_BASE_MODULE = getenv('CUSTOM_BASE_MODULE')
    DEBUG = getenv('DEBUG', False)

    @property
    def DATABASE_URL(self):
        return getenv("DATABASE_URL", 'sqlite:///default.db')

    @property
    def BOT_TOKEN(self):
        return getenv("BOT_TOKEN")
