from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.core.create_aquarium import CreateAquarium
from project.core.create_decoration import CreateDecoration
from project.core.helper import Helper
from project.core.create_fish import CreateFish


class Controller:
    AQUARIUM_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in CreateAquarium.AQUARIUM_TYPES:
            return "Invalid aquarium type."
        aquarium = CreateAquarium.create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in CreateDecoration.DECORATION_TYPES:
            return "Invalid decoration type."
        decoration = CreateDecoration.create_decoration(decoration_type)
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = Helper.find_decoration_by_type(self.decorations_repository.decorations,
                                                    decoration_type)
        aquarium = Helper.find_aquarium_by_name(self.aquariums, aquarium_name)
        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}."
        if aquarium is not None:
            self.decorations_repository.remove(decoration)
            self.aquariums[aquarium].add_decoration(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = Helper.find_aquarium_by_name(self.aquariums, aquarium_name)
        if fish_type not in CreateFish.FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."
        fish = CreateFish.create_fish(fish_type, fish_name, fish_species, price)
        result = aquarium.add_fish(fish)
        return result

    def feed_fish(self, aquarium_name: str):
        aquarium = Helper.find_aquarium_by_name(self.aquariums, aquarium_name)
        aquarium.feed()
        fish_count = len(aquarium.fish)
        return f"Fish fed: {fish_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = Helper.find_aquarium_by_name(self.aquariums, aquarium_name)
        fish_price = sum(fish.price for fish in aquarium.fish)
        decorations_price = sum(decoration.price for decoration in aquarium.decorations)
        value = fish_price + decorations_price
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"

        return result.strip()

