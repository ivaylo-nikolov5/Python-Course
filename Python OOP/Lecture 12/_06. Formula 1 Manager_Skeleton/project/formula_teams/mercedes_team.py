from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        expenses = 200000
        prizes = {
            1: 1000000,
            2: 500000,
            5: 100000,
            7: 50000
        }
        if race_pos in prizes:
            revenue += prizes[race_pos]

        revenue -= expenses
        self.budget += revenue
        self.position = race_pos
        self.revenue = revenue
        return f"The revenue after this race is {revenue}$. Current budget {self.budget}$"