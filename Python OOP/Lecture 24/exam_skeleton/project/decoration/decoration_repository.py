from project.core.create_decorations import CreateDecorations


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        decoration_obj = CreateDecorations.create_decoration(decoration)
        self.decorations.append(decoration_obj)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        return "None"
