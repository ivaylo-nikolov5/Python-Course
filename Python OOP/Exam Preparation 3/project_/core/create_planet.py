from project_.planet.planet import Planet


class CreatePlanet:
    @staticmethod
    def create_planet(name, items):
        planet = Planet(name)
        planet.items = items
        return planet
