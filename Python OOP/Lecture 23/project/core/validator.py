class Validator:
    @staticmethod
    def check_if_model_is_less_than_four_letters(model: str):
        if len(model) < 4:
            raise ValueError(f"Model {model} is less than 4 symbols!")

    @staticmethod
    def validate_speed_limit_range(speed_limit: int, min_speed: int, max_speed: int):
        if not min_speed <= speed_limit <= max_speed:
            raise ValueError(f"Invalid speed limit! Must be between {min_speed} and {max_speed}!")

    @staticmethod
    def validate_if_name_is_whitespace_or_empty_string(name: str):
        if not name.strip():
            raise ValueError("Name should contain at least one character!")

