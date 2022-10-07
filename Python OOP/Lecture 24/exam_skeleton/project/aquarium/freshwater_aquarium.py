from project.aquarium.base_aquarium import BaseAquarium
from project.fish.freshwater_fish import FreshwaterFish


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, 50)

    @property
    def get_type(self):
        return FreshwaterFish.__name__

