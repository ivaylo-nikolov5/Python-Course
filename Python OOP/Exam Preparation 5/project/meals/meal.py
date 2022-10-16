from abc import ABC, abstractmethod

from project.core.validator import Validator


class Meal(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Name cannot be an empty string!"
        Validator.check_if_string_is_empty_or_whitespace(value, message)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        message = "Invalid price!"
        Validator.check_if_value_is_less_or_equal_to_zero(value, message)
        self.__price = value

    @abstractmethod
    def details(self):
        pass
