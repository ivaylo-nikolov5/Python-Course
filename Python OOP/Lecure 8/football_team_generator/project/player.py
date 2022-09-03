class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        res = f"Player: {self.__name}"
        res += f"\nSprint: {self.__sprint}"
        res += f"\nDribble: {self.__dribble}"
        res += f"\nPassing: {self.__passing}"
        res += f"\nShooting: {self.__shooting}"

        return res


