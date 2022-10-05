from project.core.create_car import CreateCar
from project.core.create_driver import CreateDriver
from project.core.validator import Validator


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        Validator.check_if_car_model_already_exists(self.cars, model)
        if car_type not in CreateCar.CAR_TYPES:
            return
        car = CreateCar.create_car(car_type, model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        Validator.check_if_driver_already_exists(self.drivers, driver_name)
        driver = CreateDriver.create_driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        pass

    def add_car_to_driver(self, driver_name: str, car_type: str):
        pass

    def add_driver_to_race(self, race_name: str, driver_name: str):
        pass

    def start_race(self, race_name: str):
        pass

