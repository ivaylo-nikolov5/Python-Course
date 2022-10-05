from project.driver import Driver


class CreateDriver:
    @staticmethod
    def create_driver(name):
        driver = Driver(name)
        return driver
