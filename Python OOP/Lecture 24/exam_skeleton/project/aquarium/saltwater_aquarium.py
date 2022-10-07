from project.aquarium.base_aquarium import BaseAquarium
from project.fish.saltwater_fish import SaltwaterFish


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, 25)

    @property
    def get_type(self):
        return SaltwaterFish.__name__

