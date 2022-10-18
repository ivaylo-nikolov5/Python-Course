from project_.core.validator import Validator
from project_.movie_specification.movie import Movie


class Fantasy(Movie):
    def __init__(self, title: str, year: int, owner: object, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        message = "Fantasy movies must be restricted for audience under 6 years!"
        Validator.check_if_number_is_below_limit(value, 6, message)
        self.__age_restriction = value

    def details(self):
        result = f"Fantasy - Title:{self.title}, Year:{self.year}, " \
                 f"Age restriction:{self.age_restriction}, " \
                 f"Likes:{self.likes}, Owned by:{self.owner.username}"
        return result