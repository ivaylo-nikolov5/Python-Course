class Validator:
    @staticmethod
    def raise_if_string_is_empty(string, message):
        if not string.strip():
            raise ValueError(message)
    @staticmethod
    def raise_if_number_is_zero_or_negative(number, message):
        if number <= 0:
            raise ValueError(message)
