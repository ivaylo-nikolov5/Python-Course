class Helper:
    @staticmethod
    def find_index(values, index):
        for idx in range(len(values)):
            if idx == index:
                return idx

        raise IndexError("Invalid index!")

    @staticmethod
    def iter_over_list_or_tuple_or_string(values, iterable):
        for el in iterable:
            values.append(el)

        return values

    @staticmethod
    def iter_over_dictionary(values, iterable: dict):
        for el in iterable.keys():
            values.append(el)

        return values

    @staticmethod
    def insert_value_in_list(values, value, index):
        if index < 0 or index > len(values):
            raise IndexError("Invalid index!")

        new_values = []

        for idx in range(len(values)):
            if idx == index:
                new_values.append(value)
            new_values.append(values[idx])

        return new_values
