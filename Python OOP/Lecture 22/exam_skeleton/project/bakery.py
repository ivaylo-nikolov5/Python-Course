class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food (self, food_type: str, name: str, price: float):
        pass

    def add_drink (self, drink_type: str, name: str, portion: int, brand:str):
        pass

    def add_table (self, table_type: str, table_number: int, capacity: int):
        pass

    def reserve_table (self, number_of_people: int):
        pass

    def order_food (self, table_number: int, *args):
        pass

    def order_drink (self, table_number: int, *args):
        pass

    def leave_table (self, table_number: int):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        pass
