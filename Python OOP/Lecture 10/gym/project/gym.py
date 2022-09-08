from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


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
        subscription = self.__find_entity_by_id(self.subscriptions, subscription_id)
        customer = self.__find_entity_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_entity_by_id(self.trainers, subscription.trainer_id)
        plan = self.__find_entity_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_entity_by_id(self.equipment, plan.equipment_id)

        result += f"\n{repr(subscription)}"
        result += f"\n{repr(customer)}"
        result += f"\n{repr(trainer)}"
        result += f"\n{repr(plan)}"
        result += f"\n{repr(equipment)}"

        return result

    def __find_entity_by_id(self, collection, entity_id):
        for entity in collection:
            if entity.id == entity_id:
                return entity
