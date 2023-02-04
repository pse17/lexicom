
IS_EXPENSIVE = 50000


class Technic:
    __slots__ = ['name', 'price', 'availability']

    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

    @property
    def category(self):
        return 'Дорогой' if self.price > IS_EXPENSIVE else 'Бюджктный'



