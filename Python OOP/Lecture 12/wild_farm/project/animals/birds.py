from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_INCREMENTAL = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOODS = ["Fruit", "Vegetable", "Meat", "Seed"]
    WEIGHT_INCREMENTAL = 0.35

    def make_sound(self):
        return "Cluck"

