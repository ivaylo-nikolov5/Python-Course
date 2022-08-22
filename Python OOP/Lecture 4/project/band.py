from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for album_ in self.albums:
            if album.name == album_.name:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):

        for album_ in self.albums:
            if album_name == album.name:
                if album_.published:
                    return f"Album has been published. It cannot be removed."
                self.albums.remove(album_)
                return f"Album {album_.name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}"

        for album in self.albums:
            result += f"\n{album.details()}"

        return result


album = Album("The Sound of Perseverance")
song = Song("Scavenger of Human Sorrow", 6.56, False)
album.add_song(song)
message = album.add_song(song)

