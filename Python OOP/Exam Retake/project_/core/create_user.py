from project_.user import User


class CreateUser:
    @staticmethod
    def create_user(username, age):
        user = User(username, age)
        return user