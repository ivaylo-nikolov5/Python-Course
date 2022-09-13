from project.animals.animal import Mammal


class Mouse(Mammal):
    EATABLE_FOOD = ["Vegetable", "Fruit"]
    WEIGHT_INCREMENTAL = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Cat(Mammal):
    EATABLE_FOOD = ["Vegetable", "Meat"]
    WEIGHT_INCREMENTAL = 0.3

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Dog(Mammal):
    EATABLE_FOOD = ["Meat"]
    WEIGHT_INCREMENTAL = 0.4

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Tiger(Mammal):
    EATABLE_FOOD = ["Meat"]
    WEIGHT_INCREMENTAL = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"