from sqlalchemy.exc import NoResultFound

from src.posts.exeptions.sqlalchemy_exeptions import NotFoundExeption
from src.posts.models.repository import Repository
from src.posts.models.items.model import Item
from src.posts.models.specification import  Specification


class ItemRepository(Repository):
    def get(self, spec: Specification):
        try:
            return self.session.query(Item).filter(spec).one()
        except NoResultFound as exc:
            raise NotFoundExeption(exc)

    def list(self, spec: Specification | None):
        try:
            if spec is None:
                return self.session.query(Item).all()
            else:
                return self.session.query(Item).filter(spec).all()
        except NoResultFound as exc:
            raise NotFoundExeption(exc)

    def save(self, obj):
        self.session.add(obj)

    def update(self, obj):
        self.session.add(obj)
