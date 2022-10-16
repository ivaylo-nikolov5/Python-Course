from project.client import Client


class CreateClient:
    @staticmethod
    def create_client(number):
        client = Client(number)
        return client