from project_.hardware.heavy_hardware import HeavyHardware
from project_.hardware.power_hardware import PowerHardware


class CreateHardware:
    hardware = {
        "Power": PowerHardware,
        "Heavy": HeavyHardware
    }

    @staticmethod
    def create_hardware(hardware_type, name: str, capacity: int, memory: int):
        hardware = CreateHardware.hardware[hardware_type](name, capacity, memory)
        return hardware
