from project.race import Race


class CreateRace:
    @staticmethod
    def create_race(name):
        race = Race(name)
        return race