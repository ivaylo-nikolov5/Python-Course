from gym.project.customer import Customer
from gym.project.equipment import Equipment
from gym.project.exercise_plan import ExercisePlan
from gym.project.subscription import Subscription
from gym.project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ""
        subscription = self.__find_entity(subscription_id, self.subscriptions)
        customer = self.__find_entity(subscription.customer_id, self.customers)
        trainer = self.__find_entity(subscription.trainer_id, self.trainers)
        equipment = self.__find_entity(subscription.exercise_id, self.equipment)
        plan = self.__find_entity(equipment.id, self.plans)

        result += f"{repr(subscription)}\n" \
                  f"{repr(customer)}\n" \
                  f"{repr(trainer)}\n" \
                  f"{repr(equipment)}\n" \
                  f"{repr(plan)}"

        return result

    @staticmethod
    def __find_entity(entity_id, entities):
        for entity in entities:
            if entity.id == entity_id:
                return entity

