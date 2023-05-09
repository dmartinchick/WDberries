import random
from config import config
# from models.items.model import Item
# TODO: пересмотреть класс Elo


class EloCalculator:
    def __init__(self, item_a: Item, item_b: Item):
        self.item_a = item_a
        self.item_b = item_b
        self.__ea, self.__eb = self.get_expected_points()
        self.__k = 30

    @property
    def item_a(self):
        return self.__item_a

    @item_a.setter
    def item_a(self, item: Item):
        self.__item_a = item

    @property
    def item_b(self):
        return self.__item_b

    @item_b.setter
    def item_b(self, item: Item):
        self.__item_b = item

    @property
    def ea(self):
        return self.__ea

    @property
    def eb(self):
        return self.__eb

    def get_expected_points(self) -> tuple:
        e_a = 1/(1 + pow(10, (self.item_a.point - self.item_b.point) / 400))
        e_b = 1/(1 + pow(10, (self.item_b.point - self.item_a.point) / 400))
        return e_a, e_b

    @staticmethod
    def rerating(item: Item, s: float, e: float, k: int):
        item.point += k*(s-e)

    def run(self, result: str):
        if result == 'draw':
            self.rerating(item=self.item_a, s=0.5, e=self.ea, k=self.__k)
            self.rerating(item=self.item_b, s=0.5, e=self.eb, k=self.__k)
        elif result == 'item a win':
            self.rerating(item=self.item_a, s=1.0, e=self.ea, k=self.__k)
            self.rerating(item=self.item_b, s=0.0, e=self.eb, k=self.__k)
        elif result == 'item b win':
            self.rerating(item=self.item_a, s=0.0, e=self.ea, k=self.__k)
            self.rerating(item=self.item_b, s=1.0, e=self.eb, k=self.__k)
        else:
            raise TypeError()
        return self.item_a.point, self.item_b.point


class Elo:
    def __init__(self, items: [Item]):
        self.items = items

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items

    def run(self):
        item_a, item_b = random.sample(self.items, 2)
        calculator = EloCalculator(item_a, item_b)
        calculator.run('item a win')

    def loop_testing(self, col: int) -> [Item]:
        count = 0
        while count != col:
            item_a, item_b = random.sample(self.items, 2)
            calculate = EloCalculator(item_a, item_b)
            item_a.point, item_b.point = calculate.run(random.choice(['draw', 'item a win', 'item b win']))
            count += 1
