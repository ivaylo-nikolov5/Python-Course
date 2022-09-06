from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.find_room(room_number)
        room.take_room(people)

    def free_room(self, room_number):
        room = self.find_room(room_number)
        room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {sum([room.guests for room in self.rooms])} total guests" \
                 f"\nFree rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}" \
                 f"\nTaken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"

        return result

    def find_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room
