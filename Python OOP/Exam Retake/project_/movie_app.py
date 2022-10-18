from project_.core.create_user import CreateUser
from project_.core.helper import Helper
from project_.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        user = CreateUser.create_user(username, age)
        message = "User already exists!"
        Helper.check_if_user_exist(self.users_collection, username, message)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        message = "This user does not exist!"
        user = None
        for user_ in self.users_collection:
            if user_.username == username:
                user = user_
                break
        if user is None:
            raise Exception(message)

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        elif movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            else:
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user = Helper.find_user(self.users_collection, username, "")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = Helper.find_user(self.users_collection, username, "")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        elif movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = Helper.find_user(self.users_collection, username, "")
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        movies = list(sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))
        result = []
        for movie in movies:
            result.append(movie.details())

        return ", ".join(result)

    def __str__(self):
        result = ""
        users = f"All users: No users." if not self.users_collection else \
            f"All users: {', '.join([x.username for x in self.users_collection])}"

        movies = "All movies: No movies." if not self.movies_collection else \
            f"All movies: {', '.join([x.title for x in self.movies_collection])}"

        result += users + "\n"
        result += movies

        return result