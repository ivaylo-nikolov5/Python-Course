from unittest import TestCase, main
from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("Khan Asparuh", 5)

    def test_constructor(self):
        self.assertEqual("Khan Asparuh", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_method_with_full_capacity(self):
        self.train.passengers.extend(["person1", "person2", "person3", "person4", "person5"])
        self.assertEqual(5, len(self.train.passengers))
        with self.assertRaises(ValueError) as ex:
            self.train.add("person6")
        expected = "Train is full"
        self.assertEqual(expected, str(ex.exception))

    def test_add_method_with_already_existing_passenger(self):
        self.train.passengers.append("person")
        with self.assertRaises(ValueError) as ex:
            self.train.add("person")
        expected = "Passenger person Exists"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(1, len(self.train.passengers))

    def test_add_method_with_correct_data(self):
        result = self.train.add("Ivan")
        expected = "Added passenger Ivan"
        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual(expected, result)

    def test_remove_method_with_not_existing_passenger(self):
        expected = "Passenger Not Found"
        self.train.add("Ivan")
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Pesho")
        self.assertEqual(expected, str(ex.exception))

    def test_remove_method_with_correct_data(self):
        expected = "Removed Ivan"
        self.train.add("Ivan")
        result = self.train.remove("Ivan")
        self.assertEqual(0, len(self.train.passengers))
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()