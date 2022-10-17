from abc import ABC, abstractmethod

from project_.core.validator import Validator


class Supply(ABC):
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Name cannot be an empty string."
        Validator.raise_if_string_is_empty(value, message)
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        message = "Energy cannot be less than zero."
        Validator.raise_if_number_is_negative(value, message)
        self.__energy = value

    @abstractmethod
    def details(self):
        pass