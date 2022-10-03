class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(value, string):
        if not value.strip():
            raise ValueError(string)