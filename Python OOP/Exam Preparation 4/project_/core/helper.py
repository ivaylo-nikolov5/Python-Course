class Helper:
    @staticmethod
    def get_item_with_name(items, name, message):
        for item in items:
            if item.name == name:
                return item

        raise Exception(message)

    @staticmethod
    def find_available_horse(horses, horse_type, message):
        while horses:
            horse = horses.pop()
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        raise Exception(message)

    @staticmethod
    def find_race(races, race_type, message):
        for race in races:
            if race.race_type == race_type:
                return race

        raise Exception(message)

    @staticmethod
    def find_if_jockey_is_already_added(races, jockey):
        for race in races:
            if jockey in race.jockeys:
                return True

        return False

    @staticmethod
    def get_winner(jockeys, race_type):
        winner_jockey = None
        winner_horse = None
        highest_speed = 0
        for jockey in jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner_jockey = jockey
                winner_horse = jockey.horse

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner_jockey.name}! " \
               f"Winner's horse: {winner_horse.name}."
