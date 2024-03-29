class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(value, string):
        if not value.strip():
            raise ValueError(string)

    @staticmethod
    def raise_if_number_is_less_or_equal_to_zero(number, string):
        if number <= 0:
            raise ValueError(string)
    @staticmethod
    def raise_if_price_is_zero_or_negative(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_table_already_exists(tables, table_number):
        for table in tables:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

    @staticmethod
    def could_not_find_table(table_number):
        return f"Could not find table {table_number}"
