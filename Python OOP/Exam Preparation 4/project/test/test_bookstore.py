from project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTest(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(50)

    def test_constructor_with_proper_books_limit(self):
        self.assertEqual(50, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_book_limit_raises_with_zero_and_negative_value(self):
        with self.assertRaises(ValueError) as ex:
            Bookstore(0)
        expected = "Books limit of 0 is not valid"
        self.assertEqual(expected, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            Bookstore(-35)
        expected = "Books limit of -35 is not valid"
        self.assertEqual(expected, str(ex.exception))

    def test_len_returns_proper_count_of_the_books(self):
        self.bookstore.availability_in_store_by_book_titles["Test"] = 17
        self.bookstore.availability_in_store_by_book_titles["Grow Business"] = 23
        result = len(self.bookstore)
        self.assertEqual(40, result)

    def test_receive_book_raises_with_non_enough_space_in_bookstore(self):
        self.bookstore.receive_book("Other Title", 43)

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Some Title", 56)
        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(ex.exception))

    def test_receive_book_with_proper_data(self):
        expected = "17 copies of Mind Your Own Business are available in the bookstore."
        result = self.bookstore.receive_book("Mind Your Own Business", 17)
        self.assertEqual(17, self.bookstore.availability_in_store_by_book_titles["Mind Your Own Business"])
        self.assertEqual(expected, result)

        expected = "47 copies of Mind Your Own Business are available in the bookstore."
        result = self.bookstore.receive_book("Mind Your Own Business", 30)
        self.assertEqual(47, self.bookstore.availability_in_store_by_book_titles["Mind Your Own Business"])
        self.assertEqual(expected, result)

    def test_sell_book_raises_with_not_existing_book(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Not Existing Book", 2)
        expected = "Book Not Existing Book doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_raises_with_not_enough_quantity_of_books(self):
        self.bookstore.receive_book("Python Masterclass", 41)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Python Masterclass", 43)
        expected = "Python Masterclass has not enough copies to sell. Left: 41"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_with_proper_data(self):
        self.bookstore.receive_book("Python Masterclass", 41)
        result = self.bookstore.sell_book("Python Masterclass", 11)
        self.assertEqual(30, self.bookstore.availability_in_store_by_book_titles["Python Masterclass"])
        self.assertEqual(11, self.bookstore.total_sold_books)
        expected = "Sold 11 copies of Python Masterclass"
        self.assertEqual(expected, result)

    def test_str_returns_proper_string(self):
        self.bookstore.receive_book("Python Masterclass", 41)
        result = str(self.bookstore)
        expected = "Total sold books: 0\n"
        expected += "Current availability: 41\n"
        expected += " - Python Masterclass: 41 copies"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
