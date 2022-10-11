class System:
    def __init__(self):
        self._hardware = []
        self._software = []

    def register_power_hardware(self, name: str, capacity: int, memory: int):
        pass

    def register_heavy_hardware(self, name: str, capacity: int, memory: int):
        pass

    def register_express_software(self, hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        pass

    def register_light_software(self, hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        pass

    def release_software_component(self, hardware_name: str, software_name: str):
        pass

    def analyze(self):
        pass

    def system_split(self):
        pass
