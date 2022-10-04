from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Dogs")

    def test_constructor(self):
        self.assertEqual(self.pet_shop.name, "Dogs")
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])



if __name__ == '__main__':
    main()

