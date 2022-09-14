from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        expenses = 200000

        if race_pos == 1:
            revenue += 1000000
        elif race_pos == 3:
            revenue += 500000

        if race_pos <= 5:
            revenue += 100000
        elif race_pos <= 7:
            revenue += 50000

        revenue -= expenses
        self.budget += revenue
        self.position = race_pos
        self.revenue = revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"