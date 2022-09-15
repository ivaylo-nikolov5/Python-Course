from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


def animal_sound(animals: list):
    result = ""
    for animal in animals:
        result += animal.make_sound() + "\n"

    return result.strip()


class Cat(Animal):
    def make_sound(self):
        return f"Meow-meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof-woof"


class Chicken(Animal):
    def make_sound(self):
        return "Pew-pew"


animals = [Cat(), Dog(), Chicken()]

print(animal_sound(animals))

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
