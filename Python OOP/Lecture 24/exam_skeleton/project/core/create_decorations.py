from project.decoration.plant import Plant
from project.decoration.ornament import Ornament


class CreateDecorations:
    DECORATIONS = {
        "Plant": Plant,
        "Ornament": Ornament
    }

    @staticmethod
    def create_decoration(decoration):
        decoration_obj = CreateDecorations.DECORATIONS[decoration]()
        return decoration_obj