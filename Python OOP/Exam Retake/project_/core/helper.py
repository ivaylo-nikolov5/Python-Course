class Helper:
    @staticmethod
    def check_if_user_exist(users, username, message):
        for user in users:
            if user.username == username:
                raise Exception(message)

    @staticmethod
    def find_user(users, username, message):
        for user in users:
            if user.username == username:
                return user

        raise Exception(message)