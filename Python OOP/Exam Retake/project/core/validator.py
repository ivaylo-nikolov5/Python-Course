class Validator:
    @staticmethod
    def check_if_string_is_empty(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def check_if_number_is_below_limit(number, limit, message):
        if number < limit:
            raise ValueError(message)