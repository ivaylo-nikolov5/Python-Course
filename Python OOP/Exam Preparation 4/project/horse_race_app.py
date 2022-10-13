from project.core.create_horse import CreateHorse
from project.core.validator import Validator


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if Validator.check_if_object_with_same_name_exists(self.horses, horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")
        horse = CreateHorse.create_horse(horse_type, horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        pass

    def create_horse_race(self, race_type: str):
        pass

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        pass

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass

    def start_horse_race(self, race_type: str):
        pass
