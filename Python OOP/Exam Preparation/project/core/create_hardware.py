from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class CreateHardware:
    hardware = {
        "Power": PowerHardware,
        "Heavy": HeavyHardware
    }

    @staticmethod
    def create_hardware(hardware_type, name: str, capacity: int, memory: int):
        hardware = hardware_type[CreateHardware.hardware](name, capacity, memory)
        return hardware
