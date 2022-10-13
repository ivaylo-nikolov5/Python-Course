from unittest import TestCase, main
from project.library import Library


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library("Name")

    def test_constructor_with_proper_name(self):
        self.assertEqual('Name', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_constructor_with_empty_string_as_name(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ""
        expected = "Name cannot be empty string!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_book_with_non_added_author(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book("Slavi Panayotov", "Top Mysteries of Bulgaria")
        expected = {"Slavi Panayotov": ["Top Mysteries of Bulgaria"]}
        self.assertEqual(expected, self.library.books_by_authors)

    def test_add_book_with_existing_author(self):
        self.library.add_book("Slavi Panayotov", "Top Mysteries of Bulgaria")
        expected = {"Slavi Panayotov": ["Top Mysteries of Bulgaria"]}
        self.assertEqual(expected, self.library.books_by_authors)

        self.library.add_book("Slavi Panayotov", "Top Mysteries of th World")
        expected = {"Slavi Panayotov": ["Top Mysteries of Bulgaria", "Top Mysteries of th World"]}
        self.assertEqual(expected, self.library.books_by_authors)

    def test_add_reader_with_non_existing_reader(self):
        self.assertEqual({}, self.library.readers)
        self.library.add_reader("Ivan")
        expected = {"Ivan": []}
        self.assertEqual(expected, self.library.readers)

        self.library.add_reader("Martin")
        expected = {"Ivan": [], "Martin": []}
        self.assertEqual(expected, self.library.readers)

    def test_add_reader_with_already_existing_reader(self):
        self.library.add_reader("Ivan")
        result = self.library.add_reader("Ivan")
        expected = "Ivan is already registered in the Name library."
        self.assertEqual(expected, result)

    def test_rent_book_with_non_existing_reader(self):
        self.library.add_reader("Ivan")
        result = self.library.rent_book("Blagoy", "Test", "test")
        expected = f"Blagoy is not registered in the Name Library."
        self.assertEqual(expected, result)

    def test_rent_book_with_non_existing_author(self):
        self.library.add_reader("Ivan")
        self.library.add_book("J.K. Rowling", "Harry Potter")
        result = self.library.rent_book("Ivan", "Bay Ivan", "test")
        expected = f"Name Library does not have any Bay Ivan's books."

    def test_rent_book_with_non_existing_book(self):
        self.library.add_reader("Ivan")
        self.library.add_book("J.K. Rowling", "Harry Potter")
        result = self.library.rent_book("Ivan", "J.K. Rowling", "Finci")
        expected = """Name Library does not have J.K. Rowling's "Finci"."""
        self.assertEqual(expected, result)

    def test_rent_book_with_proper_data(self):
        self.library.add_reader("Ivan")
        self.library.add_book("J.K. Rowling", "Harry Potter")
        self.library.rent_book("Ivan", "J.K. Rowling", "Harry Potter")

        expected = {"Ivan": [{"J.K. Rowling": "Harry Potter"}]}
        self.assertEqual(expected, self.library.readers)

        expected = {"J.K. Rowling": []}
        self.assertEqual(expected, self.library.books_by_authors)


if __name__ == '__main__':
    main()
