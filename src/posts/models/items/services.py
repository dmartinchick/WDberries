from src.posts.models.specification import Specification
# from src.posts.models.container import Container
from src.posts.exeptions.sqlalchemy_exeptions import NotFoundExeption
from src.posts.models.unit_of_work import UnitOfWork
from src.posts.models.repository import Repository
from src.posts.models.items.model import Item


def get_item(spec: Specification,
             repository: Repository):
    try:
        return repository.get(spec)
    except NotFoundExeption:
        return None


def list_items(spec: Specification | None,
               repository: Repository):
    try:
        return repository.list(spec)
    except NotFoundExeption:
        return None


def add_item(item: Item, unit_of_work: UnitOfWork):
    unit_of_work.repository.save(item)
    unit_of_work.commit()


def update_item(item: Item, unit_of_work: UnitOfWork):
    unit_of_work.repository.update(item)
    unit_of_work.commit()
