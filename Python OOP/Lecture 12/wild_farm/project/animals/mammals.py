from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ["Vegetable", "Fruit"]
    WEIGHT_INCREMENTAL = 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_INCREMENTAL = 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOODS = ["Vegetable, Meat"]
    WEIGHT_INCREMENTAL = 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_INCREMENTAL = 1

    def make_sound(self):
        return "ROAR!!!"
