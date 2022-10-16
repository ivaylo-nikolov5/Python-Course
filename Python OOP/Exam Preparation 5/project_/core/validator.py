class Validator:
    @staticmethod
    def check_if_mobile_number_is_valid(number: str):
        if not(number[0] == "0" and len(number) == 10 and number.isdigit()):
            raise ValueError("Invalid phone number!")

    @staticmethod
    def check_if_string_is_empty_or_whitespace(text, message):
        if text.strip() == "":
            raise ValueError(message)

    @staticmethod
    def check_if_value_is_less_or_equal_to_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_menu_is_not_ready(menu):
        if len(menu) < 5:
            raise Exception("The menu is not ready!")

    @staticmethod
    def check_if_meal_exists(meals_list, meals_orders):
        meals_ = []
        for searched_meal, quantity in meals_orders.items():
            for meal in meals_list:
                if searched_meal == meal.name:
                    if quantity > meal.quantity:
                        raise Exception(f"Not enough "
                                        f"quantity of {meal.__class__.__name__}: {meal.name}!")
                    meals_.append([meal, quantity])
                    break
            else:
                raise Exception(f"{searched_meal} is not on the menu!")


        return meals_

