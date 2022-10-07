from abc import ABC, abstractmethod

from project.core.validator import Validator
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    @property
    @abstractmethod
    def get_type(self):
        pass

    def calculate_comfort(self):
        return sum(fish.comfort for fish in self.fish)

    def add_fish(self, fish: BaseFish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        elif fish.__class__.__name__ != self.get_type:
            return "Water not suitable."
        self.fish.append(fish)
        return f"Successfully added {self.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\nFish: "
        result += "none" if not self.fish else f"{' '.join(fish.name for fish in self.fish)}"
        result += f"\nDecorations: {len(self.decorations)}\n" \
                  f"Comfort: {self.calculate_comfort()}"

        return result
