from abc import ABC, abstractmethod
from project_.core.validator import Validator


class Car(ABC):
    MIN_SPEED_LIMIT = 0
    MAX_SPEED_LIMIT = 0

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.check_if_model_is_less_than_four_letters(value)
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.validate_speed_limit_range(value, self.MIN_SPEED_LIMIT, self.MAX_SPEED_LIMIT)
        self.__speed_limit = value
