from project.core.create_horse import CreateHorse
from project.core.create_horse_race import CreateHorseRace
from project.core.create_jockey import CreateJockey
from project.core.helper import Helper
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
        jockey = CreateJockey.create_jockey(self.jockeys, jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = CreateHorseRace.create_horse_race(self.horse_races, race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        message = "Jockey {jockey_name} could not be found!"
        jockey = Helper.get_item_with_name(self.jockeys, jockey_name, message)
        message = f"Horse breed {horse_type} could not be found!"
        horse = Helper.find_available_horse(self.horses, horse_type, message)

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        message = f"Race {race_type} could not be found!"
        race = Helper.find_race(self.horse_races, race_type, message)
        message = f"Jockey {jockey_name} could not be found!"
        jockey = Helper.get_item_with_name(self.jockeys, jockey_name, message)

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        elif Helper.find_if_jockey_is_already_added(self.horse_races, jockey):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        message = f"Race {race_type} could not be found!"
        race = Helper.find_race(self.horse_races, race_type, message)
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = Helper.get_winner(race.jockeys, race_type)
        return winner

