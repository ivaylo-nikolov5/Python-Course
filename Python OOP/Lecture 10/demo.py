from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld

from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld

import unittest

class TestsMovieWorld(unittest.TestCase):
    def test_dvd_class_method(self):
        dvd = DVD.from_date(1, "A", "16.10.1997", 18)
        self.assertEqual(dvd.creation_year, 1997)
