from config import logger
from src.posts.models.container import Container
from src.posts.models.unit_of_work import UnitOfWork
from src.posts.models.items.model import Item
from src.posts.models.items.specifications import ItemById, IsActiveItems, ItemWithoutImg
from src.posts.models.items.services import get_item, list_items, add_item, update_item


class ItemCommands:
    def __init__(self, container: Container):
        self.__container = container
        self.__specification = None

    def is_exists(self, item_id: int) -> bool:
        return True if self.get_item_by_id(item_id) is not None else False

    def get_item_by_id(self, item_id: int) -> Item | None:
        self.__specification = ItemById().is_satisfied(item_id)
        return get_item(self.__specification, self.__container.item_repository)

    def get_active_items(self) -> [Item]:
        self.__specification = IsActiveItems().is_satisfied(True)
        return list_items(self.__specification, self.__container.item_repository)

    def get_all_items(self) -> [Item]:
        return list_items(self.__specification, self.__container.item_repository)

    def get_items_without_img(self) -> [Item]:
        self.__specification = ItemWithoutImg().is_satisfied(None)
        return list_items(self.__specification, self.__container.item_repository)

    def get_items_with_img(self) -> [Item]:
        self.__specification = ~ ItemWithoutImg().is_satisfied(None)
        return list_items(self.__specification, self.__container.item_repository)

    def set_item(self,
                 item_id: int,
                 brand: str,
                 name: str,
                 price: float,
                 img_url: str | None = None):
        if not self.is_exists(item_id):
            new_item = Item(
                id=item_id,
                brand=brand,
                name=name,
                price=price,
                img_url=img_url
            )
            add_item(new_item, self.__container.item_uow)
        else:
            logger.warning(f"Неудачная попытка добавления платья в БД ")

    def set_item_img(self, item_id: int, img_url: str):
        if self.is_exists(item_id):
            item = self.get_item_by_id(item_id)
            item.img_url = img_url
            update_item(item, self.__container.item_uow)

    def add_points(self, item_id: int, points: int):
        if self.is_exists(item_id):
            item = self.get_item_by_id(item_id)
            item.point += points
            update_item(item, self.__container.item_uow)

    def take_away_points(self, item_id: int, points: int):
        if self.is_exists(item_id):
            item = self.get_item_by_id(item_id)
            item.point -= points
            update_item(item, self.__container.item_uow)

    def deactivate_item(self, item_id: int):
        if self.is_exists(item_id):
            item = self.get_item_by_id(item_id)
            item.is_active = False
            update_item(item, self.__container.item_uow)

    def activate_item(self, item_id: int):
        if self.is_exists(item_id):
            item = self.get_item_by_id(item_id)
            item.is_active = True
            update_item(item, self.__container.item_uow)
