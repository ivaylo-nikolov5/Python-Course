from project_.software.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", capacity_consumption, memory_consumption)
        self.capacity_consumption += self.capacity_consumption // 2
        self.memory_consumption -= self.memory_consumption // 2
