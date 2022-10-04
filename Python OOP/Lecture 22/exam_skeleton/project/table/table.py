from abc import ABC, abstractmethod
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.core.validator import Validator


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_if_number_is_less_or_equal_to_zero(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        if self.capacity <= number_of_people:
            self.is_reserved = True
            self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = self.bill(self.food_orders) + self.bill(self.drink_orders)
        return bill

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}"\
                   f"Type: {self.__class__.__name__}"\
                   f"Capacity: {self.capacity}"

    @staticmethod
    def bill(orders: list):
        total = 0
        for order in orders:
            total += order.price

        return total