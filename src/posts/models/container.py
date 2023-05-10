from src.posts.models.session import Session
from src.posts.models.unit_of_work import AlchemyUnitOfWork
# TODO: переписать импорты ниже
from src.posts.models.items.repository import ItemRepository
from src.posts.models.items.model import Item


# TODO:> https://python-dependency-injector.ets-labs.org/examples/fastapi-sqlalchemy.html#fastapi-sqlalchemy-example

class Container:

    session_creator = Session()
    item_repository = ItemRepository(session=session_creator)
    item_uow = AlchemyUnitOfWork(repository=item_repository)
