from project_.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        capacity = software.capacity_consumption
        memory = software.memory_consumption
        if self.capacity >= capacity and self.memory >= memory:
            self.software_components.append(software)
            return
        raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)
