from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class CreateSoftware:
    software = {
        "Express": ExpressSoftware,
        "Light": LightSoftware
    }

    @staticmethod
    def create_software(name: str, capacity_consumption: int, memory_consumption: int):
        software = CreateSoftware.create_software(name, capacity_consumption, memory_consumption)
        return software
