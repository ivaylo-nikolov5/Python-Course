from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class CreateAstronaut:
    astronaut_types = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }

    @staticmethod
    def create_astronaut(astronaut_type, name):
        if astronaut_type not in CreateAstronaut.astronaut_types:
            raise Exception("Astronaut type is not valid!")
        astronaut = CreateAstronaut.astronaut_types[astronaut_type](name)
        return astronaut
