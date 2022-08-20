class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        free_space = self.capacity - self.content
        if not free_space >= ml:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        free_space = self.capacity - self.content
        return f"{free_space} ml left"


glass = Glass()
glass.fill(50)
res = glass.info()
