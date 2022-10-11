from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Test", 100)

    def test_constructor_initialize_properly(self):
        expected = ["white", "yellow", "blue", "green", "red"]
        self.assertEqual("Test", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(expected, self.factory.valid_ingredients)

    def test_add_ingredient_raises_not_allowed_ingredient(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("black", 10)
        expected = "Ingredient of type black not allowed in PaintFactory"
        self.assertEqual(expected, str(ex.exception))

    def test_add_ingredient_raises_not_enough_space(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("white", 150)
        expected = "Not enough space in factory"
        self.assertEqual(expected, str(ex.exception))

    def test_add_ingredient_adds_the_ingredient_in_the_dict_with_given_value(self):
        self.assertEqual({}, self.factory.ingredients)
        self.factory.add_ingredient("white", 20)
        self.assertEqual({"white": 20}, self.factory.ingredients)
        self.factory.add_ingredient("green", 20)
        self.assertEqual({"white": 20, "green": 20}, self.factory.ingredients)
        self.factory.add_ingredient("green", 20)
        self.assertEqual({"white": 20, "green": 40}, self.factory.ingredients)

    def test_remove_ingredient_with_non_existing_ingredient(self):
        self.factory.add_ingredient("white", 20)
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("black", 50)
        self.assertEqual("No such ingredient in the factory", str(ex.exception))

    def test_remove_less_than_zero_ingredients(self):
        self.factory.add_ingredient("white", 20)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("white", 50)
        expected = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected, str(ex.exception))

    def test_repr_returns_proper_string(self):
        self.factory.add_ingredient("white", 20)
        self.factory.add_ingredient("green", 20)
        result = repr(self.factory)
        expected = "Factory name: Test with capacity 100.\nwhite: 20\ngreen: 20\n"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    main()

