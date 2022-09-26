class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

import unittest
class WorkerTests(unittest.TestCase):
    def test_worker_is_initialized_correctly(self):
        worker = Worker("Test", 1000, 10)
        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_if_energy_is_incremented_after_rest(self):
        worker = Worker("Test", 1000, 10)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_if_error_is_raised_after_working_with_low_energy(self):
        worker = Worker("Test", 1000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_error_is_raised_after_working_with_negative_energy(self):
        worker = Worker("Test", 1000, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_money_is_increased_with_salary_correctly(self):
        worker = Worker("Test", 1000, 10)
        worker.work()
        self.assertEqual(1000, worker.money)

    def test_if_worker_energy_is_decreased(self):
        worker = Worker("Test", 1000, 10)
        worker.work()
        self.assertEqual(9, worker.energy)

    def test_if_the_get_info_method_returns_proper_string(self):
        worker = Worker("Test", 1000, 10)
        expected = f'Test has saved 0 money.'
        self.assertEqual(expected, worker.get_info())


if __name__ == "__main__":
    unittest.main()