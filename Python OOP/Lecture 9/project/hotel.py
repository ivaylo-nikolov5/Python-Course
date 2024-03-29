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
        self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        current_room.take_room(people)

    def free_room(self, room_number):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        current_room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {sum([room.guests for room in self.rooms])} total guests" \
                 f"\nFree rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}" \
                 f"\nTaken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"

        return result
