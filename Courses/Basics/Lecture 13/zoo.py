class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animals}"

        return result


zoo_name = input()

zoo = Zoo(zoo_name)

lines_count = int(input())

for i in range(lines_count):
    info = input().split(" ")
    animal_type = info[0]
    animal = info[1]
    zoo.add_animal(animal_type, animal)


additional_info = input()

print(zoo.get_info(additional_info))