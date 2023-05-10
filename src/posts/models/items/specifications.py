from src.posts.models.items.model import Item
from src.posts.models.specification import Specification


class ItemById(Specification):
    def is_satisfied(self, candidate):
        return Item.id == candidate


class IsActiveItems(Specification):
    def is_satisfied(self, candidate):
        return Item.is_active == candidate


class ItemWithoutImg(Specification):
    def is_satisfied(self, candidate):
        return Item.img_url == candidate
