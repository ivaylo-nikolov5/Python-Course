class Validator:
    @staticmethod
    def check_if_name_is_empty_string_or_space(name, message):
        if name.strip() == "":
            raise ValueError(message)