class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = self.food_cost + sum([toy_cost for toy_cost in toys_cost])
