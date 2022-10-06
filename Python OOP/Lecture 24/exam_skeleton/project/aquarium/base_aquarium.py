from abc import ABC, abstractmethod
from project.core.validator import Validator
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    POSSIBLE_FISH_TYPES = [FreshwaterFish, SaltwaterFish]

    @abstractmethod
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
        if len(fish) == self.capacity:
            return "Not enough capacity."
        elif fish.__class__.__name__ in BaseAquarium.POSSIBLE_FISH_TYPES:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.feed()

    def __str__(self):
        result = f"{self.name}:\n"
        if not self.fish:
            result += "Fish: none\n"
        else:
            result += f"Fish: {' '.join(fish.name for fish in self.fish)}\n" \

        result += f"Decorations: {len(self.decorations)}\n" \
                  f"Comfort: {self.calculate_comfort()}"

        return result
