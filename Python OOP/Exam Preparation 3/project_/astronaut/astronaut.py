from abc import ABC, abstractmethod
from project_.core.validator import Validator


class Astronaut(ABC):
    OXYGEN_DECREASE = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []
        self.successful_missions = 0
        self.not_completed_missions = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Astronaut name cannot be empty string or whitespace!"
        Validator.check_if_name_is_empty_string_or_space(value, message)
        self.__name = value

    def breathe(self):
        self.oxygen -= self.OXYGEN_DECREASE

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

