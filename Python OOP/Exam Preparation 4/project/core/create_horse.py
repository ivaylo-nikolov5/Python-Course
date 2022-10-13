from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class CreateHorse:
    horse_types = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    @staticmethod
    def create_horse(horse_type, name, speed):
        if horse_type in CreateHorse.horse_types:
            horse = CreateHorse.horse_types[horse_type](name, speed)
            return horse
