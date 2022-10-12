from project.core.validator import Validator


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Planet name cannot be empty string or whitespace!"
        Validator.check_if_name_is_empty_string_or_space(value, message)
        self.__name = value