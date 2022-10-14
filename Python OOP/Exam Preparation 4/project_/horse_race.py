from project_.core.validator import Validator


class HorseRace:
    race_types = ["Winter", "Spring", "Autumn", "Summer"]
    
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []
        
    @property
    def race_type(self):
        return self.__race_type
    
    @race_type.setter
    def race_type(self, value):
        message = "Race type does not exist!"
        Validator.check_is_race_type_is_valid(HorseRace.race_types, value, message)
        self.__race_type = value
        