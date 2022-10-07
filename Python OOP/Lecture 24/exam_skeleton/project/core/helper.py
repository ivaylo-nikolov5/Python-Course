class Helper:
    @staticmethod
    def find_decoration_by_type(decorations, decoration_type):
        for decoration in decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        return None

    @staticmethod
    def find_aquarium_by_name(aquariums, name):
        for aquarium in aquariums:
            if aquarium.name == name:
                return aquarium
        return None
