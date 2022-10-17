from project_.core.helper import Helper
from project_.player import Player
from project_.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            already_added = False
            for player_ in self.players:
                if player_.name == player.name:
                    already_added = True
                    break
            if not already_added:
                added_players.append(player)
                self.players.append(player)

        return f"Successfully added: {', '.join([x.name for x in added_players])}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = Helper.find_player_by_name(self.players, player_name)
        if player is None or sustenance_type not in ("Food", "Drink"):
            return

        message = "There are no food supplies left!"
        if sustenance_type == "Drink":
            "There are no drink supplies left!"
        supply = Helper.check_if_supply_type_is_available(self.supplies, sustenance_type, message)

        if player.stamina == player.STAMINA_MAX_VALUE:
            return f"{player_name} have enough stamina."
        player.stamina += supply.energy
        self.supplies.remove(supply)
        if player.stamina > player.STAMINA_MAX_VALUE:
            player.stamina = player.STAMINA_MAX_VALUE

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = Helper.find_player_by_name(self.players, first_player_name)
        player2 = Helper.find_player_by_name(self.players, second_player_name)

        if player1.stamina == 0:
            return f"Player {player1.name} does not have enough stamina."
        elif player2.stamina == 0:
            return f"Player {player2.name} does not have enough stamina."


        current_attacker = player1 if player1.stamina < player2.stamina else player2
        second_attacker = player1 if current_attacker == player2 else player2

        winner = None

        second_attacker.stamina -= current_attacker.stamina / 2
        if second_attacker.stamina <= 0:
            second_attacker.stamina = 0
            winner = current_attacker

        current_attacker.stamina -= second_attacker.stamina / 2
        if current_attacker.stamina <= 0:
            current_attacker.stamina = 0
            winner = second_attacker

        if winner is None:
            winner = player1 if player1.stamina > player2.stamina else player2

        return f"Winner: {winner.name}"

    def next_day(self):
        self.players = Helper.reduce_health_on_next_day(self.players)

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))

        for supply in self.supplies:
            result.append(supply.details())

        return "\n".join(result)