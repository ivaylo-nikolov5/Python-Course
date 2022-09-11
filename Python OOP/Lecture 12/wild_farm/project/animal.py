from abc import ABC, abstractmethod

from project.food import Vegetable


class Animal(ABC):
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass



class Bird(ABC, Animal):
    def __init__(self, name, weight, food_eaten, wing_size):
        super(Animal).__init__(name, weight, food_eaten)
        self.wing_size = wing_size


class Mammal(ABC, Animal):
    def __init__(self, name, weight, food_eaten, living_region ):
        super(Animal).__init__(name, weight, food_eaten)
        self.wing_size = living_region
