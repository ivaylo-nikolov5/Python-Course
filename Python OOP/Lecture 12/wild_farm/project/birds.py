from project.animal import Bird


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        pass


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        if food.__class__.__name__ == "Vegetable" or food.__class__.__name__ == "Fruit":
            self.weight += food.quantity * 0.25
