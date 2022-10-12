from collections import deque


class Helper:
    @staticmethod
    def find_by_name(objects, name):
        for obj in objects:
            if obj.name == name:
                return obj

    @staticmethod
    def find_suitable_astronauts(astronauts):
        astronauts_ = [x for x in astronauts if x.oxygen > 30]
        if not astronauts_:
            raise Exception("You need at least one astronaut to explore the planet!")
        astronauts_ = list(sorted(astronauts_, key=lambda x: x.oxygen))
        if len(astronauts_) > 5:
            astronauts_ = astronauts_[:5]

        return astronauts_

    @staticmethod
    def explore_planet(astronauts: deque, items):
        number_of_astronauts = 0
        for i in range(len(astronauts)):
            astronaut = astronauts.popleft()
            while astronaut.oxygen > 0:
                items.pop()
                astronaut.breathe()
            number_of_astronauts += 1

            if not astronauts:
                return "Mission is not completed."
        return number_of_astronauts