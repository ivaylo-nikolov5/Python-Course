class Helper:
    @staticmethod
    def find_player_by_name(players, name):
        for player in players:
            if player.name == name:
                return player

    @staticmethod
    def check_if_supply_type_is_available(supplies, supply_type, message):
        for supply in reversed(supplies):
            if supply.__class__.__name__ == supply_type:
                return supply
        raise Exception(message)

    @staticmethod
    def reduce_health_on_next_day(players):
        for player in players:
            player.stamina -= player.age * 2
            if player.stamina < 0:
                player.stamina = 0

        return players



