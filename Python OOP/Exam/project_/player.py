from project_.core.validator import Validator


class Player:
    STAMINA_MAX_VALUE = 100

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance = self.stamina < 100
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        message = "Name not valid!"
        Validator.raise_if_string_is_empty(value, message)
        self.__name = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        message = "The player cannot be under 12 years old!"
        Validator.raise_if_number_is_lower_than_limit(value, 12, message)
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        message = "Stamina not valid!"
        Validator.raise_if_number_not_in_range(value, 0, Player.STAMINA_MAX_VALUE, message)
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"