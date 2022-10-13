class Validator:
    @staticmethod
    def raise_if_string_contains_only_whitespaces_or_empty(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_lower_than_limit(limit, number, message):
        if number < limit:
            raise ValueError(message)
