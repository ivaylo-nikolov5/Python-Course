class Validator:
    @staticmethod
    def check_if_model_is_less_than_four_letters(model: str):
        if len(model) < 4:
            raise ValueError(f"Model {model} is less than 4 symbols!")

    @staticmethod
    def validate_speed_limit_range(speed_limit: int, min_speed: int, max_speed: int):
        if not min_speed <= speed_limit <= max_speed:
            raise ValueError(f"Invalid speed limit! Must be between {min_speed} and {max_speed}!")

    @staticmethod
    def validate_if_name_is_whitespace_or_empty_string(name: str, message: str):
        if not name.strip():
            raise ValueError(message)

    @staticmethod
    def check_if_car_model_already_exists(cars, model):
        for car in cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

    @staticmethod
    def check_if_driver_already_exists(drivers, name):
        for driver in drivers:
            if driver.name == name:
                raise Exception(f"Driver {name} is already created!")

