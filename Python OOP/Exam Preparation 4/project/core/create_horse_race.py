from project.horse_race import HorseRace


class CreateHorseRace:
    @staticmethod
    def create_horse_race(races, race_type):
        for race in races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        return race