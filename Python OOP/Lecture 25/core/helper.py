class Helper:
    @staticmethod
    def find_index(values, index):
        for idx in range(len(values)):
            if idx == index:
                return values[idx]

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