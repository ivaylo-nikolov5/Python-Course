from project_.core.validator import Validator
from project_.jockey import Jockey


class CreateJockey:
    @staticmethod
    def create_jockey(jockeys, name, age):
        if not Validator.check_if_object_with_same_name_exists(jockeys, name):
            jockey = Jockey(name, age)
            return jockey
        raise Exception(f"Jockey {name} has been already added!")