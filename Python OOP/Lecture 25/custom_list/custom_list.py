from core.helper import Helper

class CustomList:
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

