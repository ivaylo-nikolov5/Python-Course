from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE_INCREMENTAL = 2

    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)
