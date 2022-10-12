from collections import deque

from project_.astronaut.astronaut_repository import AstronautRepository
from project_.core.create_astronaut import CreateAstronaut
from project_.core.create_planet import CreatePlanet
from project_.core.helper import Helper
from project_.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str) :
        check_if_exist = Helper.find_by_name(self.astronaut_repository.astronauts, name)
        if check_if_exist is not None:
            return f"{name} is already added."
        astronaut = CreateAstronaut.create_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        check_if_exist = Helper.find_by_name(self.planet_repository.planets, name)
        if check_if_exist is not None:
            return f"{name} is already added."
        planet = CreatePlanet.create_planet(name, items)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = Helper.find_by_name(self.astronaut_repository.astronauts, name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = Helper.find_by_name(self.planet_repository, planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")
        astronauts = Helper.find_suitable_astronauts(self.astronaut_repository.astronauts)
        astronauts = deque(astronauts)
        number_of_astronauts = Helper.explore_planet(astronauts, planet.items)
        if not isinstance(number_of_astronauts, int):
            return number_of_astronauts
        return f"Planet: {planet_name} was explored. {astronauts} astronauts participated in collecting items."


    def report(self):
        result = ""


