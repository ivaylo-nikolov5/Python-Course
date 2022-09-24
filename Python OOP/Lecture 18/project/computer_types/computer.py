from abc import ABC, abstractmethod


class Computer(ABC):
    VALID_COMPUTER_TYPES = ["Laptop", "Desktop Computer"]

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    @abstractmethod
    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"



