from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, name: str, budget: float, members_count: int):
        super().__init__(name, budget, members_count)
        self.room_cost = 10
