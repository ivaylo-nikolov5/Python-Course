class Validator:
    @staticmethod
    def raise_if_string_contains_only_whitespaces_or_empty(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_lower_than_limit(limit, number, message):
        if number < limit:
            raise ValueError(message)

    @staticmethod
    def raise_if_length_is_lower_than_limit(limit, value, message):
        if len(value) < limit:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_higher_than_limit(limit, number, message):
        if number > limit:
            raise ValueError(message)

    @staticmethod
    def check_is_race_type_is_valid(race_types, race_type, message):
        if race_type not in race_types:
            raise ValueError(message)

    @staticmethod
    def check_if_object_with_same_name_exists(objects, name):
        for obj in objects:
            if obj.name == name:
                return True
        return False
