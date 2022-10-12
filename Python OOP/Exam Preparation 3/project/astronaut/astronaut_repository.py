from project.astronaut.astronaut import Astronaut
from project.core.helper import Helper


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        astronaut = Helper.find_by_name(self.astronauts, name)
        return astronaut

