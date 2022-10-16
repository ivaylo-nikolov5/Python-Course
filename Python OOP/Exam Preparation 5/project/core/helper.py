from project.core.create_client import CreateClient


class Helper:
    @staticmethod
    def check_if_client_exists(clients, number):
        for client in clients:
            if client.phone_number == number:
                return True, client

        client = CreateClient.create_client(number)
        return False, client

    @staticmethod
    def get_meal(meals, meal):
        for meal_ in meals:
            if meal_.name == meal.name:
                return meal_

    @staticmethod
    def raise_if_shopping_cart_is_empty(cart):
        if not cart:
            raise Exception("There are no ordered meals!")
