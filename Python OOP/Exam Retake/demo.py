from project.plantation import Plantation

plantation = Plantation(10)
plantation.workers = ["Ivan", "Andrey"]
plantation.plants = {"Ivan": ["rice", "smth"], "Andrey": ["sugar cane", "smth"]}
print(plantation)