from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        expenses = 250000

        if race_pos == 1:
            revenue += 1500000
        elif race_pos == 2:
            revenue += 800000

        if race_pos <= 8:
            revenue += 20000
        elif race_pos <= 10:
            revenue += 10000

        revenue -= expenses
        self.budget += revenue
        self.position = race_pos
        self.revenue = revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"