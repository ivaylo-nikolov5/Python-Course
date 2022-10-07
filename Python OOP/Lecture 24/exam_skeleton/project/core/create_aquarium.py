from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium


class CreateAquarium:
    AQUARIUM_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    @staticmethod
    def create_aquarium(aquarium_type, name):
        return CreateAquarium.AQUARIUM_TYPES[aquarium_type](name)

