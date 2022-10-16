from project.core.create_client import CreateClient
from project.core.helper import Helper
from project.core.validator import Validator
from project.meals.meal import Meal


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        client = CreateClient.create_client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ("Starter", "MainDish", "Dessert"):
                self.menu.append(meal)

    def show_menu(self):
        Validator.raise_if_menu_is_not_ready(self.menu)
        result = []
        for meal in self.menu:
            result.append(meal.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        Validator.raise_if_menu_is_not_ready(self.menu)
        is_exist, client = Helper.check_if_client_exists(self.clients_list, client_phone_number)
        if not is_exist:
            self.clients_list.append(client)
        meals = Validator.check_if_meal_exists(self.menu, meal_names_and_quantities)

        bill = 0
        for meal, quantity in meals:
            client.shopping_cart.append(meal)
            bill += meal.price * quantity
            index = self.menu.index(meal)
            meal = self.menu[index]
            meal.quantity -= quantity

        client.bill += bill
        meal_names = ", ".join(meal.name for meal in client.shopping_cart)
        return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = Helper.check_if_client_exists(self.clients_list, client_phone_number)[1]
        Helper.raise_if_shopping_cart_is_empty(client.shopping_cart)
        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = Helper.check_if_client_exists(self.clients_list, client_phone_number)[1]
        Helper.raise_if_shopping_cart_is_empty(client.shopping_cart)
        client.shopping_cart = []
        bill = client.bill
        client.bill = 0
        FoodOrdersApp.receipt_id += 1
        return f"Receipt #{FoodOrdersApp.receipt_id} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
