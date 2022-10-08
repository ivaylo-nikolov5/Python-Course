class Helper:
    @staticmethod
    def find_index(values, index):
        for idx in range(len(values)):
            if idx == index:
                return values[idx]

        raise IndexError("Invalid index!")