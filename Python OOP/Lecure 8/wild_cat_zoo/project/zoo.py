class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity - 1:
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity - 1:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        to_pay = 0
        for worker in self.workers:
            to_pay += worker.salary

        if to_pay > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= to_pay
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        to_tend = 0
        for animal in self.animals:
            to_tend += animal.money_for_care

        if to_tend > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= to_tend
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal.__repr__())
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal.__repr__())
            else:
                cheetahs.append(animal.__repr__())

        result += f"\n----- {len(lions)} Lions:"

        for lion in lions:
            result += f"\n{lion}"

        result += f"\n----- {len(tigers)} Tigers:"

        for tiger in tigers:
            result += f"\n{tiger}"

        result += f"\n----- {len(cheetahs)} Cheetahs:"

        for cheetah in cheetahs:
            result += f"\n{cheetah.__repr__()}"

    def workers_status(self):
        result = f"You have {len(self.workers)} animals"
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker.__repr__())
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker.__repr__())
            else:
                vets.append(worker.__repr__())

        result += f"\n----- {len(keepers)} Keepers:"

        for keeper in keepers:
            result += f"\n{keeper}"

        result += f"\n----- {len(caretakers)} Caretakers:"

        for caretaker in caretakers:
            result += f"\n{caretaker}"

        result += f"\n----- {len(vets)} Vets:"

        for vet in vets:
            result += f"\n{vet}"

