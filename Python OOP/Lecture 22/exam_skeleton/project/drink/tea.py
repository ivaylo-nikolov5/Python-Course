from project.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name, portion, price, brand):
        super().__init__(name, portion, price, brand)
        self.price = 2.5
