from project_.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140
    SPEED_INCREMENT = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)