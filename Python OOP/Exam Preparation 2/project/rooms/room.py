from project.core.validator import Validator
from project.core.helper import Helper


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        Validator.raise_if_value_is_negative(value, "Expenses cannot be negative")
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        expenses = Helper.get_expenses(args)
        return expenses
