from project_.core.validator import Validator


class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_if_name_is_whitespace_or_empty_string(value, "Name cannot be an empty string!")
        self.__name = value
