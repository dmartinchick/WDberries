from abc import ABC, abstractmethod
from src.posts.models.session import Session
from src.posts.models.specification import Specification


class Repository(ABC):

    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def get(self, spec: Specification):
        raise NotImplementedError

    @abstractmethod
    def list(self, spec: Specification):
        raise NotImplementedError

    @abstractmethod
    def save(self, obj):
        raise NotImplementedError

    @abstractmethod
    def update(self, obj):
        raise NotImplementedError
