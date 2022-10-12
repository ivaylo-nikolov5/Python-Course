class Helper:
    @staticmethod
    def find_by_name(objects, name):
        for obj in objects:
            if obj.name == name:
                return obj
