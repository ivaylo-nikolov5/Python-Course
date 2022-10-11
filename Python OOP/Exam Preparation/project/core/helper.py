class Helper:
    @staticmethod
    def find_hardware(hardware, name):
        for el in hardware:
            if el.name == name:
                return el
        return "Hardware does not exist"

    @staticmethod
    def find_software(software, name):
        for el in software:
            if el.name == name:
                return el
        return "Software does not exist"
