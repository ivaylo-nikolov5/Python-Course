from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class CreateDecoration:
    DECORATION_TYPES = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    @staticmethod
    def create_decoration(decoration_type):
        decoration = CreateDecoration.DECORATION_TYPES[decoration_type]()
        return decoration
