from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise ValueError("Not all teams have registered for the season.")
        leading_team = "Mercedes" if self.mercedes_team.position > self.red_bull_team.position else "Red Bull"
        mercedes_revenue = 0

        return f"Red bull: {self.red_bull_team.cal}. Mercedes: { Mercedes revenue message }. { team with better position } is ahead at the { race name } race."