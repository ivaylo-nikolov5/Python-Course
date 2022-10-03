from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water

class Bakery:
    FOOD_TYPES = [Bread, Cake]
    DRINK_TYPES = [Tea, Water]

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

    def add_drink(self, drink_type, name: str, portion: int, brand:str):
        if self.check_name_existence(self.drinks_menu, name):
            self.raise_already_in_the_menu(drink_type, name)
        elif drink_type in self.DRINK_TYPES:
            self.drinks_menu.append(Bakery.DRINK_TYPES[drink_type](name, portion, brand))

    def add_table(self, table_type: str, table_number: int, capacity: int):
        pass

    def reserve_table(self, number_of_people: int):
        pass

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