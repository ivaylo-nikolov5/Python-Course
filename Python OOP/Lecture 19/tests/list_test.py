from unittest import TestCase, main
from extended_list import IntegerList


class ListTests(TestCase):
    def test_if_constructor_works_properly(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual([1, 2, 3, 4, 5], test_list.get_data())

        new_test_list = IntegerList(1, 2, 3, "t", 4, 5)
        self.assertEqual([1, 2, 3, 4, 5], new_test_list.get_data())

    def test_the_get_data_method(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual([1, 2, 3, 4, 5], test_list.get_data())

    def test_add_method(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        test_list.add(6)
        self.assertEqual([1, 2, 3, 4, 5, 6], test_list.get_data())

    def test_add_method_raises(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        expected = "Element is not Integer"

        with self.assertRaises(Exception) as ex:
            test_list.add("t")
        self.assertEqual(expected, str(ex.exception))

        with self.assertRaises(Exception) as ex:
            test_list.add(3.14)
        self.assertEqual(expected, str(ex.exception))

    def test_remove_index_method(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        test_list.remove_index(3)
        self.assertEqual([1, 2, 3, 5], test_list.get_data())

        test_list.remove_index(0)
        self.assertEqual([2, 3, 5], test_list.get_data())

    def test_remove_index_method_raises(self):
        test_list = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as ex:
            test_list.remove_index(5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method(self):
        test_list = IntegerList(1, 2, 3, 4, 5)

        result = test_list.get(4)
        self.assertEqual(5, result)

        result = test_list.get(0)
        self.assertEqual(1, result)

    def test_get_method_raises(self):
        test_list = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as ex:
            test_list.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method(self):
        test_list = IntegerList(1, 2, 3, 4, 6)
        test_list.insert(4, 5)
        self.assertEqual([1, 2, 3, 4, 5, 6], test_list.get_data())

    def test_insert_method_raises_index_error(self):
        test_list = IntegerList(1, 2, 3, 4, 6)
        with self.assertRaises(IndexError) as ex:
            test_list.insert(5, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_raises_value_error(self):
        test_list = IntegerList(1, 2, 3, 4, 6)

        with self.assertRaises(ValueError) as ex:
            test_list.insert(4, "5")
        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            test_list.insert(4, 0.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_method(self):
        test_list = IntegerList(1, 2, 3, 4, 69)
        result = test_list.get_biggest()

        self.assertEqual(69, result)

        test_list.remove_index(4)
        result = test_list.get_biggest()

        self.assertEqual(4, result)

    def test_get_index_method(self):
        test_list = IntegerList(1, 2, 3, 4, 69)
        result = test_list.get_index(69)

        self.assertEqual(4, result)

        test_list.remove_index(4)
        result = test_list.get_index(4)

        self.assertEqual(3, result)


if __name__ == '__main__':
    main()
