from project.core.create_hardware import CreateHardware
from project.core.create_software import CreateSoftware
from project.core.helper import Helper


class System:
    FAIL_MESSAGE = "Hardware does not exist"

    def __init__(self):
        self._hardware = []
        self._software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = CreateHardware.create_hardware("Power", name, capacity, memory)
        return power_hardware

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = CreateHardware.create_hardware("Heavy", name, capacity, memory)
        return heavy_hardware

    def register_express_software(self, hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        software = CreateSoftware.create_software(name, capacity_consumption, memory_consumption)
        hardware = Helper.find_hardware(self._hardware, hardware_name)
        if hardware == System.FAIL_MESSAGE:
            return System.FAIL_MESSAGE
        hardware.install(software)
        self._software.append(software)

    def register_light_software(self, hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        software = CreateSoftware.create_software(name, capacity_consumption, memory_consumption)
        hardware = Helper.find_hardware(self._hardware, hardware_name)
        if hardware == System.FAIL_MESSAGE:
            return System.FAIL_MESSAGE
        hardware.install(software)
        self._software.append(software)

    def release_software_component(self, hardware_name: str, software_name: str):
        hardware = Helper.find_hardware(self._hardware, hardware_name)
        software = Helper.find_software(self._software, software_name)
        if isinstance(hardware, str) or isinstance(software, str):
            return "Some of the components do not exist"
        hardware.uninstall(software)
        self._software.remove(software)

    def analyze(self):
        software_memory_consumption = sum([x.memory_consumption for x in self._software])
        hardware_memory_consumption = sum([x.memory_consumption for x in self._hardware])

        software_capacity_consumption = sum([x.capacity_consumption for x in self._software])
        hardware_capacity_consumption = sum([x.capacity_consumption for x in self._hardware])
        result = f"System Analysis\n" \
                 f"Hardware Components: {len(self._hardware)}\n" \
                 f"Software Components: {len(self._software)}\n" \
                 f"Total Operational Memory: {software_memory_consumption} / {hardware_memory_consumption}\n" \
                 f"Total Capacity Taken: {software_capacity_consumption} / {hardware_capacity_consumption}"

        return result


    def system_split(self):
        for component in self._hardware:
            express_software_components = len([x for x in component.software_components if x.software_type == "Express"])
            light_software_components = len([x for x in component.software_components if x.software_type == "Light"])

            software_memory_usage = sum([x.memory_consumption for x in component.software_components])
            software_capacity_usage = sum([x.capacity_consumption for x in component.software_components])

            software_components = ', '.join([x.name for x in component.software_components]) if \
                component.software_components else None
            result = f"Hardware Component - {component.name}\n" \
                     f"Express Software Components: {express_software_components}\n" \
                     f"Light Software Components: {light_software_components}\n" \
                     f"Memory Usage: {software_memory_usage} / {component.memory}\n" \
                     f"Capacity Usage: {software_capacity_usage} / {component.capacity}\n" \
                     f"Type: {component.hardware_type}\n" \
                     f"Software Components: {software_components}"

            return result

