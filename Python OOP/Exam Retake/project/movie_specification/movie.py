from abc import ABC, abstractmethod
from project.core.validator import Validator


class Movie(ABC):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        message = "The title cannot be empty string!"
        Validator.check_if_string_is_empty(value, message)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        message = "Movies weren't made before 1888!"
        Validator.check_if_number_is_below_limit(value, 1888, message)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if value.__class__.__name__ != "User":
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @abstractmethod
    def details(self):
        pass
    