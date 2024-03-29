class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

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
        result += self.status(self.animals, "Lion")
        result += self.status(self.animals, "Tiger")
        result += self.status(self.animals, "Cheetah")

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"
        result += self.status(self.workers, "Keeper")
        result += self.status(self.workers, "Caretaker")
        result += self.status(self.workers, "Vet")

        return result

    def status(self, entities, searched_entity):
        result = ""
        filtered = []
        for entity in entities:
            if entity.__class__.__name__ == searched_entity:
                filtered.append(entity)

        result += f"\n----- {len(filtered)} {searched_entity}s:"
        for entity in filtered:
            result += f"\n{repr(entity)}"

        return result
