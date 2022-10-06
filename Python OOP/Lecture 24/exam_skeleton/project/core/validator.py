class Validator:
    @staticmethod
    def raise_if_value_is_empty_string(value, text):
        if not value.srtip():
            raise ValueError(text)

    @staticmethod
    def raise_if_value_is_zero_or_negative(value, text):
        if value <= 0:
            raise ValueError(text)