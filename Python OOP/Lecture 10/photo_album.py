from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for x in range(pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {self.photos[page].index(label) + 1}"
        return f"No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            if page:
                result += f"{'[] '* len(page)}".strip()
                result += "\n-----------\n"
            else:
                result += "\n-----------\n"
        return result

album = PhotoAlbum(5)
for _ in range(12):
    album.add_photo("asdf")
result = album.display().strip()
print(result)

print("\n-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")