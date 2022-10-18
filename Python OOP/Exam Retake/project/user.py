from project.core.validator import Validator


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        message = "Invalid username!"
        Validator.check_if_string_is_empty(value, message)
        self.__username = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        message = "Users under the age of 6 are not allowed!"
        Validator.check_if_number_is_below_limit(value, 6, message)
        self.__age = value
        
    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}"]
        result.append("Liked movies:")
        liked_movies = "No movies liked." if not self.movies_liked else "\n".join(self.movies_liked)
        result.append(liked_movies)
        result.append("Owned movies:")
        owned_movies = "No movies owned." if not self.movies_owned else "\n".join(self.movies_owned)
        result.append(owned_movies)

        return "\n".join(result)

