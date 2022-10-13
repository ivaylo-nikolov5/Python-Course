from abc import ABC
from project.core.validator import Validator


class Horse(ABC):
    MAXIMUM_SPEED = 0
    SPEED_INCREMENT = 0

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        message = f"Horse name {value} is less than 4 symbols!"
        Validator.raise_if_length_is_lower_than_limit(4, value, message)
        self.__name = value
        
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        message = "Horse speed is too high!"
        Validator.raise_if_number_is_higher_than_limit(self.MAXIMUM_SPEED, value, message)
        self.__speed = value

    def train(self):
        if self.speed + self.SPEED_INCREMENT > self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED
        else:
            self.speed += self.SPEED_INCREMENT
