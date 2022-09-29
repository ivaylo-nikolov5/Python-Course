from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def test_constructor(self):
        dog = Mammal("Test", "dog", "woof")
        self.assertEqual("Test", dog.name)
        self.assertEqual("dog", dog.type)
        self.assertEqual("woof", dog.sound)
        self.assertEqual("animals", dog._Mammal__kingdom)

    def test_make_sound_method(self):
        cat = Mammal("Stalin", "cat", "meow")
        sound = cat.make_sound()
        expected = "Stalin makes meow"
        self.assertEqual(expected, sound)

    def test_get_kingdom_method(self):
        wolf = Mammal("Jack", "wolf", "woof")
        expected = "animals"
        self.assertEqual(expected, wolf.get_kingdom())

    def test_info_method(self):
        monkey = Mammal("Mongo", "monkey", "wa")
        expected = "Mongo is of type monkey"
        self.assertEqual(expected, monkey.info())


if __name__ == '__main__':
    main()
