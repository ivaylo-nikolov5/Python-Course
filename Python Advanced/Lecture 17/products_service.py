import json


def get_all_products():
    with open("./db/products.txt", "r") as file:
        return [json.loads(x.strip()) for x in file]
