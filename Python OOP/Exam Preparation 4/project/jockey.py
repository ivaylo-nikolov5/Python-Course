from project.core.validator import Validator


class Jockey:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Name should contain at least one character!"
        Validator.raise_if_string_contains_only_whitespaces_or_empty(value, message)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        message = "Jockeys must be at least 18 to participate in the race!"
        Validator.raise_if_number_is_lower_than_limit(18, value, message)
        self.__age = value
