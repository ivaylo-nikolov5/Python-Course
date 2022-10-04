from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.core.validator import Validator


class Bakery:
    FOOD_TYPES = [Bread, Cake]
    DRINK_TYPES = [Tea, Water]
    TABLE_TYPES = [InsideTable, OutsideTable]

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type, name: str, price: float):
        if self.check_name_existence(self.food_menu, name):
            self.raise_already_in_the_menu(food_type, name)
        elif food_type in Bakery.FOOD_TYPES:
            self.food_menu.append(Bakery.FOOD_TYPES[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name: str, portion: int, brand:str):
        if self.check_name_existence(self.drinks_menu, name):
            self.raise_already_in_the_menu(drink_type, name)
        elif drink_type in self.DRINK_TYPES:
            self.drinks_menu.append(Bakery.DRINK_TYPES[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number: int, capacity: int):
        Validator.raise_if_table_already_exists(self.tables_repository, table_number)
        if table_type in Bakery.TABLE_TYPES:
            self.tables_repository.append(Bakery.TABLE_TYPES[table_type](table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        available_table = self.find_not_reserved_table(number_of_people)
        if not available_table:
            return f"No available table for {number_of_people} people"
        table_number, table = available_table
        self.tables_repository[table].reserved = True
        return f"Table {table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        pass

    def order_drink(self, table_number: int, *args):
        pass

    def leave_table(self, table_number: int):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        pass

    @staticmethod
    def check_name_existence(sequence, name):
        for item in sequence:
            if item.name == name:
                return True
        return False

    @staticmethod
    def raise_already_in_the_menu(product_type, name):
        raise ValueError(f"{product_type} {name} is already in the menu!")

    def find_not_reserved_table(self, people_count):
        for table in self.tables_repository:
            if not table.reserved and table.capacity >= people_count:
                return [table.table_number, table]
        return False
