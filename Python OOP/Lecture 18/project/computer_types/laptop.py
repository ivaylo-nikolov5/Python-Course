from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}
    AVAILABLE_RAMS = {pow(2, ram): pow(2, ram) * 100 for ram in range(1, 7)}

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in Laptop.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop computer {self.manufacturer} {self.model}!")
        if ram not in Laptop.AVAILABLE_RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        cpu_price = Laptop.AVAILABLE_PROCESSORS[processor]
        ram_price = Laptop.AVAILABLE_RAMS[ram]
        self.price += cpu_price + ram_price
        return f"{repr(Computer)} for {self.price}$."

