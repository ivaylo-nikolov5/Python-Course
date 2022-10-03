from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    def __init__(self, name, portion, price):
        super().__init__(name, portion, price)
        self.portion = 200

