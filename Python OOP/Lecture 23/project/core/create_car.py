from project.car.sports_car import SportsCar
from project.car.muscle_car import MuscleCar


class CreateCar:
    CAR_TYPES = {
        "SportsCar": SportsCar,
        "MuscleCar": MuscleCar
    }

    @staticmethod
    def create_car(car_type: str, model: str, speed_limit: int):
        car = CreateCar.CAR_TYPES[car_type](model, speed_limit)
        return car


