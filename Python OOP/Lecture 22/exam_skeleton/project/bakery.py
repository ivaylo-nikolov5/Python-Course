from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.core.validator import Validator


class Bakery:
    FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake
    }
    DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water
    }
    TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if self.check_name_existence(self.food_menu, name):
            self.raise_already_in_the_menu(food_type, name)
        elif food_type in Bakery.FOOD_TYPES:
            food = Bakery.FOOD_TYPES[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name: str, portion: int, brand:str):
        if self.check_name_existence(self.drinks_menu, name):
            self.raise_already_in_the_menu(drink_type, name)
        elif drink_type in self.DRINK_TYPES:
            drink = Bakery.DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number: int, capacity: int):
        Validator.raise_if_table_already_exists(self.tables_repository, table_number)
        if table_type in Bakery.TABLE_TYPES:
            table = Bakery.TABLE_TYPES[table_type](table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        available_table = self.find_not_reserved_table(number_of_people)
        if not available_table:
            return f"No available table for {number_of_people} people"
        table_number, table = available_table
        table.reserve(number_of_people)
        return f"Table {table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        self.return_if_table_not_exist(table_number)
        result = self.return_orders(table_number, args, self.food_menu)
        return result

    def order_drink(self, table_number: int, *args):
        self.return_if_table_not_exist(table_number)
        result = self.return_orders(table_number, args, self.drinks_menu)
        return result

    def leave_table(self, table_number: int):
        table = self.find_table(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        result = f"Table: {table_number}\nBill: {bill:f2}"
        return result

    def get_free_tables_info(self):
        result = self.get_free_tables()
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income}lv"

    @staticmethod
    def check_name_existence(sequence, name):
        for item in sequence:
            if item.name == name:
                return True
        return False

    @staticmethod
    def raise_already_in_the_menu(product_type, name):
        raise Exception(f"{product_type} {name} is already in the menu!")

    def find_not_reserved_table(self, people_count):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= people_count:
                return [table.table_number, table]
        return False

    def find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def return_product_orders(self, bakery_name, orders, menu):
        existing_product_result = ""
        not_existing_products_result = ""

        for order in orders:
            for product in menu:
                if product.name == order:
                    existing_product_result += f"{repr(product)}\n"
                    break
            else:
                not_existing_products_result += f"{order}\n"

        existing_product_result += f"{bakery_name} does not have in the menu:\n"
        existing_product_result += not_existing_products_result

        return existing_product_result.strip()

    def return_if_table_not_exist(self, table_number):
        if not self.find_table(table_number):
            return Validator.could_not_find_table(table_number)

    def return_orders(self, table_number, orders, menu):
        result = f"Table {table_number} ordered:\n"
        result += " " + self.return_product_orders(self.name, orders, menu)
        return result

    def get_free_tables(self):
        result = ""
        for table in self.tables_repository:
            info = table.free_table_info()
            if info is not None:
                result += info + "\n"

        return result




