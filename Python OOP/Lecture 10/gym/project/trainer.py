class Trainer:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.get_next_id()

    @staticmethod
    def get_next_id():
        return Trainer.id + 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"