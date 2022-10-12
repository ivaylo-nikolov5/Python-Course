class Validator:
    @staticmethod
    def raise_if_value_is_negative(value, message):
        if value < 0:
            raise ValueError(message)