from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        expenses = 250000
        prizes = {
            1: 150000,
            2: 800000,
            8: 20000,
            10: 10000
        }
        if race_pos in prizes:
            revenue += prizes[race_pos]

        revenue -= expenses
        self.budget += revenue
        return f"The revenue after this race is {revenue}$. Current budget {self.budget}$"