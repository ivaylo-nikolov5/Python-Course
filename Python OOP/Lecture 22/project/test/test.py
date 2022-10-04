from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Dogs")

    def test_constructor(self):
        self.assertEqual(self.pet_shop.name, "Dogs")
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])

    def test_add_food_method(self):
        self.pet_shop.add_food("Bones", 50)
        result = {"Bones": 50}
        self.assertEqual(self.pet_shop.food, result)

        self.pet_shop.add_food("Meat", 20)
        result = {"Bones": 50, "Meat": 20}
        self.assertEqual(self.pet_shop.food, result)

        returned_string = self.pet_shop.add_food("Meat", 20)
        result = {"Bones": 50, "Meat": 40}
        self.assertEqual(self.pet_shop.food, result)
        expected = f"Successfully added 20.00 grams of Meat."
        self.assertEqual(expected, returned_string)

        returned_string = self.pet_shop.add_food("Meat", 1200.67)
        expected = f"Successfully added 1200.67 grams of Meat."
        self.assertEqual(expected, returned_string)

    def test_add_food_method_raises_with_zero_and_negative_value(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("Bones", 0)
        expected = 'Quantity cannot be equal to or less than 0'
        self.assertEqual(expected, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("Bones", -12)
        expected = 'Quantity cannot be equal to or less than 0'
        self.assertEqual(expected, str(ex.exception))

    def test_add_pet_method(self):
        result = self.pet_shop.add_pet("Archie")
        expected = "Successfully added Archie."
        self.assertEqual(expected, result)

        result = self.pet_shop.add_pet("Jack")
        expected = "Successfully added Jack."
        self.assertEqual(expected, result)

    def test_add_pet_method_raises_with_already_added_pet(self):
        result = self.pet_shop.add_pet("Archie")
        expected = "Successfully added Archie."
        self.assertEqual(expected, result)

        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Archie")
        expected = "Cannot add a pet with the same name"
        self.assertEqual(expected, str(ex.exception))

    def test_feed_pet_method_raises_with_not_existing_pet(self):
        self.pet_shop.add_food("Bones", 50)

        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Bones", "Archie")
        expected = "Please insert a valid pet name"
        self.assertEqual(expected, str(ex.exception))

    def test_feed_pet_method_with_not_existing_food(self):
        self.pet_shop.add_pet("Archie")
        self.pet_shop.add_food("Bones", 50)
        result = self.pet_shop.feed_pet("Chocolate Cake", "Archie")
        expected = "You do not have Chocolate Cake"
        self.assertEqual(expected, result)

    def test_feed_pet_method_with_low_food_quantity(self):
        self.pet_shop.add_pet("Archie")
        self.pet_shop.add_food("Bones", 50)
        result = self.pet_shop.feed_pet("Bones", "Archie")
        expected = "Adding food..."
        self.assertEqual(1050, self.pet_shop.food["Bones"])
        self.assertEqual(expected, result)

    def test_feed_method_with_proper_data(self):
        self.pet_shop.add_pet("Archie")
        self.pet_shop.add_food("Bones", 550)
        result = self.pet_shop.feed_pet("Bones", "Archie")
        expected = "Archie was successfully fed"
        self.assertEqual(self.pet_shop.food["Bones"], 450)
        self.assertEqual(expected, result)

    def test_if_the_repr_method_returns_correct_string(self):
        self.pet_shop.add_pet("Archie")
        self.pet_shop.add_pet("Jack")
        self.pet_shop.add_pet("Stalin")

        expected = f'Shop Dogs:\n' \
                    f'Pets: Archie, Jack, Stalin'

        result = repr(self.pet_shop)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()

