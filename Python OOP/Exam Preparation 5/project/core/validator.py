class Validator:
    @staticmethod
    def check_if_mobile_number_is_valid(number: str):
        if not(number[0] == "0" and len(number) == 10 and number.isdigit()):
            raise ValueError("Invalid phone number!")