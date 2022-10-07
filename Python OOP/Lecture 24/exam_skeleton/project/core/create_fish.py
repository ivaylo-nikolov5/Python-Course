from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class CreateFish:
    FISH_TYPES = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    @staticmethod
    def create_fish(fish_type, name, species, price):
        fish = CreateFish.FISH_TYPES[fish_type](name, species, price)
        return fish