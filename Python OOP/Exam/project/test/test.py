from project.movie import Movie
from unittest import TestCase, main


class MovieTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Home Alone", 1992, 9)

    def test_constructor_sets_the_attributes_properly(self):
        self.assertEqual("Home Alone", self.movie.name)
        self.assertEqual(1992, self.movie.year)
        self.assertEqual(9, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_with_correct_data(self):
        self.movie.name = "Home alone"
        self.assertEqual("Home alone", self.movie.name)

    def test_name_setter_raises_with_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        expected = "Name cannot be an empty string!"
        self.assertEqual(expected, str(ex.exception))

    def test_year_setter_with_correct_data(self):
        self.movie.year = 1899
        self.assertEqual(1899, self.movie.year)

    def test_year_setter_raises_with_invalid_year(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1800
        expected = "Year is not valid!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_actor_with_proper_data(self):
        self.movie.add_actor("Harry")
        self.assertEqual(["Harry"], self.movie.actors)

    def test_add_actor_raises_with_already_existing_actor(self):
        self.movie.actors = ["Harry", "Murf", "Kevin"]
        result = self.movie.add_actor("Kevin")
        expected = "Kevin is already added in the list of actors!"
        self.assertEqual(expected, result)

    def test_greater_than_returns_this_movie_has_better_rating(self):
        other_movie = Movie("Home Alone 2", 1999, 9)
        result = self.movie > other_movie
        expected = '"Home Alone 2" is better than "Home Alone"'
        self.assertEqual(expected, result)

    def test_greater_than_returns_other_movie_has_better_rating(self):
        other_movie = Movie("Home Alone 2", 1999, 9)
        result = other_movie > self.movie
        expected = '"Home Alone" is better than "Home Alone 2"'
        self.assertEqual(expected, result)

    def test_repr(self):
        self.movie.actors = ["Harry", "Murf", "Kevin"]
        expected = f"Name: Home Alone\n" \
                 f"Year of Release: 1992\n" \
                 f"Rating: 9.00\n" \
                 f"Cast: Harry, Murf, Kevin"
        result = repr(self.movie)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()