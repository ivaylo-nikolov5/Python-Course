from abc import ABC, abstractmethod
from project.core.validator import Validator
from project.core.calculations import Calculations


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_value_is_empty_string(value,
                                                 "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        comfort = sum(dec.comfort for dec in self.decorations)
        return comfort

    def add_fish(self, fish):
        pass

    def remove_fish(self, fish):
        pass

    def add_decoration(self, decoration):
        pass

    def feed(self, ):
        pass

    def __str__(self, ):
        pass
