from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
    AVAILABLE_RAMS = {pow(2, ram): pow(2, ram) * 100 for ram in range(1, 8)}

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in DesktopComputer.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram not in DesktopComputer.AVAILABLE_RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        cpu_price = DesktopComputer.AVAILABLE_PROCESSORS[processor]
        ram_price = DesktopComputer.AVAILABLE_RAMS[ram]
        self.price += cpu_price + ram_price
        return f"{repr(Computer)} for {self.price}$."