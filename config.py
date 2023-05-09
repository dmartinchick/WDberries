from abc import ABC, abstractmethod
from dataclasses import dataclass
from environs import Env
from loguru import logger


@dataclass
class DbConfig(ABC):

    @abstractmethod
    def get_url(self):
        pass


@dataclass
class DbSqlLiteConfig(DbConfig):
    db_name: str

    def get_url(self):
        return f"sqlite:///{self.db_name}"


@dataclass
class DbPGConfig(DbConfig):
    host: str
    password: str
    port: int
    user: str
    db_name: str

    def get_url(self):
        # 'postgresql+psycopg2://user:password@hostname:port/database_name'
        return f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}'


class ConfigSingleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfigSingleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, path: str):
        self.path = path
        self.env = Env()
        self.env.read_env(self.path)
        self.__db = DbPGConfig(
            host=self.env.str('PG_DB_HOST'),
            password=self.env.str('PG_DB_PASSWORD'),
            port=self.env.int('PG_DB_PORT'),
            user=self.env.str('PG_DB_USER'),
            db_name=self.env.str('PG_DB_NAME')
        )
        self.__proxies = {"http": self.env.str('PROXIES')}

    @property
    def db(self):
        return self.__db

    @property
    def proxies(self):
        return self.__proxies
