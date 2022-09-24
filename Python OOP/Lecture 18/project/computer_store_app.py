from project.computer_types.laptop import Laptop
from project.computer_types.desktop_computer import DesktopComputer


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Laptop":
            laptop = Laptop(manufacturer, model)
            self.warehouse.append(laptop)
            return laptop.configure_computer(processor, ram)
        elif type_computer == "Desktop Computer":
            desktop = DesktopComputer(manufacturer, model)
            self.warehouse.append(desktop)
            return desktop.configure_computer(processor, ram)
        return f"{type_computer} is not a valid type computer!"

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                profit = client_budget - computer.price
                self.warehouse.remove(computer)
                self.profits += profit
                return f"{repr(computer)} sold for {client_budget}$."
        return "Sorry, we don't have a computer for you."

