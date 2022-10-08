from core.helper import Helper


class CustomList:
    iterables = {
        list: Helper.iter_over_list_or_tuple_or_string,
        tuple: Helper.iter_over_list_or_tuple_or_string,
        dict: Helper.iter_over_dictionary,
        str: Helper.iter_over_list_or_tuple_or_string
    }

    def __init__(self):
        self.__values = []

    def get_list(self):
        return self.__values

    def append(self, value):
        self.__values.append(value)

    def remove(self, index):
        value = Helper.find_index(self.__values, index)
        self.__values.remove(value)
        return value

    def get(self, index):
        value = Helper.find_index(self.__values, index)
        return value

    def extend(self, iterable):
        if type(iterable) not in self.iterables:
            raise ValueError("Value not iterable!")
        result = self.iterables[type(iterable)](self.__values, iterable)
        return result


