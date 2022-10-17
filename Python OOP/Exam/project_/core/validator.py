class Validator:
    @staticmethod
    def raise_if_string_is_empty(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_negative(number, message):
        if number < 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_lower_than_limit(number, limit, message):
        if number < limit:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_not_in_range(number, min_, max_, message):
        if number < min_ or number > max_:
            raise ValueError(message)