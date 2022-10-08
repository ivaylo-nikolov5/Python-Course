from unittest import TestCase, main
from custom_list.custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.test_list = CustomList()

    def get_list_returns_the_list(self):
        self.assertEqual([], self.test_list.get_list)

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



if __name__ == '__main__':
    main()