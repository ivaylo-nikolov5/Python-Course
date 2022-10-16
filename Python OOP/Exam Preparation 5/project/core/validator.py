class Validator:
    @staticmethod
    def check_if_mobile_number_is_valid(number: str):
        if not(number[0] == "0" and len(number) == 10 and number.isdigit()):
            raise ValueError("Invalid phone number!")

    @staticmethod
    def check_if_string_is_empty_or_whitespace(text, message):
        if text.strip() == "":
            raise ValueError(message)

    @staticmethod
    def check_if_value_is_less_or_equal_to_zero(value, message):
        if value <= 0:
            raise ValueError(message)
