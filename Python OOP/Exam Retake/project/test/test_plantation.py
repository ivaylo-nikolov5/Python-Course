from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTest(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_constructor_properly_initialize(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_with_negative_number(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -20
        expected = "Size must be positive number!"
        self.assertEqual(expected, str(ex.exception))

    def test_hire_worker_raises(self):
        self.plantation.workers = ["Ivan"]
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Ivan")
        expected = "Worker already hired!"
        self.assertEqual(expected, str(ex.exception))

    def test_hire_worker_with_valid_data(self):
        result = self.plantation.hire_worker("Ivan")
        self.assertEqual(["Ivan"], self.plantation.workers)
        expected = "Ivan successfully hired."
        self.assertEqual(expected, result)

    def test_dunder_len_returns_the_length_of_the_plants(self):
        self.plantation.plants = {"a": "ab", "b": "abc", "c": "abcd"}
        self.assertEqual(9, len(self.plantation))

    def test_planting_with_non_existing_worker(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Ivan", "sugar cane")
        expected = "Worker with name Ivan is not hired!"
        self.assertEqual(expected, str(ex.exception))

    def test_planting_with_more_quantity(self):
        self.plantation.plants = {"Ivan": ["idk what is that", "a", "b", "a", "b", "a", "b", "a", "b", "a", "b"]}
        self.plantation.workers = ["Ivan"]
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Ivan", "plant with long name")
        expected = "The plantation is full!"
        self.assertEqual(expected, str(ex.exception))

    def test_planting_with_worker_who_already_has_been_planting(self):
        self.plantation.plants = {"Ivan": ["wheat"]}
        self.plantation.workers = ["Ivan"]
        result = self.plantation.planting("Ivan", "rice")
        self.assertEqual({"Ivan": ["wheat", "rice"]}, self.plantation.plants)
        self.assertEqual("Ivan planted rice.", result)

    def test_planting_with_new_worker(self):
        self.plantation.workers = ["Ivan"]
        result = self.plantation.planting("Ivan", "rice")
        self.assertEqual({"Ivan": ["rice"]}, self.plantation.plants)
        self.assertEqual("Ivan planted it's first rice.", result)

    def test_dunder_str(self):
        self.plantation.workers = ["Ivan", "Andrey"]
        self.plantation.plants = {"Ivan": ["rice", "smth"], "Andrey": ["sugar cane", "smth"]}
        result = str(self.plantation)
        expected = "Plantation size: 10\n" \
                   "Ivan, Andrey\n" \
                   "Ivan planted: rice, smth\n" \
                   "Andrey planted: sugar cane, smth"
        self.assertEqual(expected, result)

    def test_dunder_repr(self):
        self.plantation.workers = ["Ivan", "Andrey"]
        result = repr(self.plantation)
        expected = "Size: 10\nWorkers: Ivan, Andrey"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
