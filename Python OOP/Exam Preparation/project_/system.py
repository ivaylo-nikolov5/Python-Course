from project_.core.create_hardware import CreateHardware
from project_.core.create_software import CreateSoftware
from project_.core.helper import Helper


class System:
    FAIL_MESSAGE = "Hardware does not exist"
    _hardware = []
    _software = []


    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = CreateHardware.create_hardware("Power", name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = CreateHardware.create_hardware("Heavy", name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        software = CreateSoftware.create_software(name, capacity_consumption, memory_consumption, "Express")
        hardware = Helper.find_hardware(System._hardware, hardware_name)
        if hardware == System.FAIL_MESSAGE:
            return System.FAIL_MESSAGE
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        software = CreateSoftware.create_software(name, capacity_consumption, memory_consumption, "Light")
        hardware = Helper.find_hardware(System._hardware, hardware_name)
        if hardware == System.FAIL_MESSAGE:
            return System.FAIL_MESSAGE
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = Helper.find_hardware(System._hardware, hardware_name)
        software = Helper.find_software(System._software, software_name)
        if isinstance(hardware, str) or isinstance(software, str):
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        software_memory_consumption = sum([x.memory_consumption for x in System._software])
        total_memory = sum(x.memory for x in System._hardware)

        software_capacity_consumption = sum([x.capacity_consumption for x in System._software])
        total_capacity = sum(x.capacity for x in System._hardware)
        result = f"System Analysis\n" \
                 f"Hardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {software_memory_consumption} / {total_memory}\n" \
                 f"Total Capacity Taken: {software_capacity_consumption} / {total_capacity}"

        return result

    @staticmethod
    def system_split():
        for component in System._hardware:
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

