from project.core.create_car import CreateCar
from project.core.create_driver import CreateDriver
from project.core.create_race import CreateRace
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
        Validator.check_if_race_already_exists(self.races, race_name)
        race = CreateRace.create_race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.check_if_driver_not_exists(driver_name)
        car = self.find_car_for_driver(car_type)
        result = ""
        if driver.car is not None:
            result = f"Driver {driver_name} changed his car from {driver.car.model} to {car.model}."
            driver.car.is_taken = False
        else:
            result = f"Driver {driver_name} chose the car {car.model}."

        driver.car = car
        car.is_taken = True
        return result

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.check_if_race_not_exists(race_name)
        driver = self.check_if_driver_not_exists(driver_name)

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.check_if_race_not_exists(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winners = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        winners = winners[:3]
        result = self.reward_race_winners(winners, race_name)
        return result


    def check_if_driver_not_exists(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver
        raise Exception(f"Driver {name} could not be found!")

    def find_car_for_driver(self, car_type):
        for index in range(1, len(self.cars) + 1):
            car = self.cars[-index]
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car

        raise Exception(f"Car {car_type} could not be found!")

    def check_if_race_not_exists(self, name):
        for race in self.races:
            if race.name == name:
                return race
        raise Exception(f"Race {name} could not be found!")

    def reward_race_winners(self, winners: list, race_name):
        result = ""
        for winner in winners:
            winner.number_of_wins += 1
            speed = winner.car.speed_limit
            result += f"Driver {winner.name} wins the {race_name} race with a speed of {speed}.\n"

        return result.strip()
