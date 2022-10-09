from unittest import TestCase, main

from core.helper import EmptyList, ValueNotExist
from custom_list.custom_list import CustomList


INVALID_INDEX = "Invalid index!"

class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.test_list = CustomList()

    def test_get_list_returns_the_list(self):
        test = CustomList()
        test._CustomList__values = [1, 2]
        result = test.get_list()
        self.assertEqual([1, 2], result)

    def test_append_adds_element_at_the_end_of_the_list(self):
        self.assertEqual([], self.test_list.get_list())
        self.test_list.append(10)
        self.assertEqual([10], self.test_list.get_list())
        self.test_list.append(20)
        self.assertEqual([10, 20], self.test_list.get_list())

    def test_remove_element_at_index_and_returns_the_value(self):
        self.test_list._CustomList__values = [10, 20, 30, 40, 50]
        element = self.test_list.remove(2)
        self.assertEqual([10, 20, 40, 50], self.test_list.get_list())
        self.assertEqual(30, element)

    def test_remove_element_with_wrong_index(self):
        self.test_list._CustomList__values = [10, 20, 30, 40, 50]
        with self.assertRaises(IndexError) as ex:
            self.test_list.remove(7)
        self.assertEqual(INVALID_INDEX, str(ex.exception))

    def test_get_value_by_index_returns_element(self):
        self.test_list._CustomList__values = [10, 20, 30, 40, 50]
        value = self.test_list.get(4)
        self.assertEqual(50, value)

    def test_get_value_with_wrong_index(self):
        self.test_list._CustomList__values = [10, 20, 30, 40, 50]
        with self.assertRaises(IndexError) as ex:
            self.test_list.get(9)
        self.assertEqual(INVALID_INDEX, str(ex.exception))

    def test_extend_with_list_and_tuple(self):
        self.test_list._CustomList__values = [10, 20]
        self.test_list.extend([30, 40])
        self.assertEqual([10, 20, 30, 40], self.test_list.get_list())

        self.test_list.extend((50, 60))
        self.assertEqual([10, 20, 30, 40, 50, 60], self.test_list.get_list())

    def test_extend_with_dict(self):
        self.test_list._CustomList__values = [10, 20]
        self.test_list.extend({30: "30", 40: "40"})
        self.assertEqual([10, 20, 30, 40], self.test_list.get_list())

    def test_extend_with_string(self):
        self.test_list._CustomList__values = [1, 2]
        self.test_list.extend("34")
        self.assertEqual([1, 2, "3", "4"], self.test_list.get_list())

    def test_insert_with_correct_index(self):
        self.test_list._CustomList__values = [10, 20, 30, 50]
        result = self.test_list.insert(3, 40)
        self.assertEqual([10, 20, 30, 40, 50], result)

    def test_insert_value_raises_with_wrong_index(self):
        self.test_list._CustomList__values = [10, 20, 30, 50]
        with self.assertRaises(IndexError) as ex:
            self.test_list.insert(9, 99)
        self.assertEqual(INVALID_INDEX, str(ex.exception))

    def test_pop_with_not_empty_list(self):
        self.test_list._CustomList__values = [10, 20, 30, 50]
        result = self.test_list.pop()
        self.assertEqual(50, result)
        self.assertEqual([10, 20, 30], self.test_list.get_list())

    def test_pop_with_empty_list(self):
        with self.assertRaises(EmptyList) as ex:
            self.test_list.pop()
        self.assertEqual("You cannot pop an item from an empty list", str(ex.exception))

    def test_clear_returns_an_empty_list(self):
        self.test_list.append(4)
        self.test_list.clear()
        self.assertEqual([], self.test_list.get_list())

    def test_index_returns_correct_index_of_the_value(self):
        self.test_list._CustomList__values = [10, 20, 30, 50]
        result = self.test_list.index(20)
        self.assertEqual(1, result)

    def test_index_raises_with_not_existing_value(self):
        self.test_list._CustomList__values = [10, 20, 30, 50]
        with self.assertRaises(ValueNotExist) as ex:
            self.test_list.index(60)
        self.assertEqual("The value is not in the list!", str(ex.exception))

    def test_count_method(self):
        self.test_list._CustomList__values = [10, 20, 30, 50, 10, 20, 50, 10]
        result = self.test_list.count(10)
        self.assertEqual(3, result)

    def test_reverse_with_not_empty_list(self):
        self.test_list._CustomList__values = [10, 20, 30, 50]
        expected = [50, 30, 20, 10]
        result = self.test_list.reverse()
        self.assertEqual(expected, result)

    def test_reverse_raises_with_empty_list(self):
        with self.assertRaises(EmptyList) as ex:
            self.test_list.reverse()
        self.assertEqual("You cannot reverse an empty list!", str(ex.exception))

    def test_copy_returns_a_proper_copy(self):
        self.test_list._CustomList__values = [10, 20, 30, 50]
        result = self.test_list.copy()
        self.assertEqual([10, 20, 30, 50], result)



if __name__ == '__main__':
    main()