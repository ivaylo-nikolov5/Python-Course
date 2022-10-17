from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTest(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Test", 100)

    def test_constructor_with_proper_data(self):
        self.assertEqual("Test", self.shopping_cart.shop_name)
        self.assertEqual(100, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_raise_name_with_non_capital_letter(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = "test"
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ex.exception))

    def test_raise_with_non_alpha_name(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = "t123"
        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ex.exception))

    def test_change_name_sets_properly_the_name(self):
        self.shopping_cart.shop_name = "Lidl"
        self.assertEqual("Lidl", self.shopping_cart.shop_name)

    def test_add_to_cart_with_product_more_expensive_than_limit(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.add_to_cart("Something", 300)
        expected = "Product Something cost too much!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_to_cart_with_proper_data(self):
        result = self.shopping_cart.add_to_cart("Bread", 2)
        expected = "Bread product was successfully added to the cart!"
        self.assertEqual(expected, result)
        self.assertEqual({"Bread": 2}, self.shopping_cart.products)

    def test_remove_from_cart_with_non_existing_name(self):
        self.shopping_cart.add_to_cart("Bread", 2)
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.remove_from_cart("Strawberries")
        expected = "No product with name Strawberries in the cart!"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({"Bread": 2}, self.shopping_cart.products)

    def test_remove_from_cart_removes_product_from_the_cart_properly(self):
        self.shopping_cart.add_to_cart("Bread", 2)
        result = self.shopping_cart.remove_from_cart("Bread")
        expected = "Product Bread was successfully removed from the cart!"
        self.assertEqual(expected, result)
        self.assertEqual({}, self.shopping_cart.products)

    def test_dunder_add_adds_two_instances_properly(self):
        first_instance = ShoppingCart("Billa", 100)
        first_instance.add_to_cart("Bread", 2)
        second_instance = ShoppingCart("Lidl", 200)
        second_instance.add_to_cart("Water", 3)
        new_instance = first_instance + second_instance
        self.assertEqual("BillaLidl", new_instance.shop_name)
        self.assertEqual(300, new_instance.budget)
        self.assertEqual({"Bread": 2, "Water": 3}, new_instance.products)

    def test_buy_products_with_not_enough_budget(self):
        self.shopping_cart.add_to_cart("Water", 3)
        self.shopping_cart.add_to_cart("Meat", 20)
        self.shopping_cart.add_to_cart("Pan", 90)

        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.buy_products()
        expected = "Not enough money to buy the products! Over budget with 13.00lv!"
        self.assertEqual(expected, str(ex.exception))

    def test_buy_products_with_enough_budget(self):
        self.shopping_cart.add_to_cart("Pan", 90)
        result = self.shopping_cart.buy_products()
        expected = 'Products were successfully bought! Total cost: 90.00lv.'
        self.assertEqual(expected, result)




if __name__ == '__main__':
    main()