from unittest import TestCase, main
from car_manager import Car


class CarTest(TestCase):
    def test_car_constructor(self):
        new_car = Car("Test", "test", 10, 100)

        self.assertEqual(new_car.make, "Test")
        self.assertEqual(new_car.model, "test")
        self.assertEqual(new_car.fuel_consumption, 10)
        self.assertEqual(new_car.fuel_capacity, 100)

    def test_make_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            new_car = Car("", "test", 10, 100)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            new_car = Car("Make", "", 10, 100)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            new_car = Car("Make", "model", 0, 100)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            new_car = Car("Make", "model", -138, 100)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            new_car = Car("Make", "model", 10, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            new_car = Car("Make", "model", 10, -348)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_raises(self):
        new_car = Car("Make", "model", 10, 100)
        with self.assertRaises(Exception) as ex:
            new_car.fuel_amount = -234
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_with_half_amount(self):
        new_car = Car("Make", "model", 10, 100)
        new_car.refuel(50)
        self.assertEqual(new_car.fuel_amount, 50)

    def test_refuel_method_with_more_fuel_than_capacity(self):
        new_car = Car("Make", "model", 10, 100)
        new_car.refuel(150)
        self.assertEqual(new_car.fuel_amount, new_car.fuel_capacity)

    def test_refuel_method_with_zero_fuel_amount(self):
        new_car = Car("Make", "model", 10, 100)
        with self.assertRaises(Exception) as ex:
            new_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_negative_fuel_amount(self):
        new_car = Car("Make", "model", 10, 100)
        with self.assertRaises(Exception) as ex:
            new_car.refuel(-12)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_method(self):
        new_car = Car("Make", "model", 10, 100)
        new_car.refuel(100)
        new_car.drive(5)
        self.assertEqual(99.5, new_car.fuel_amount)

    def test_drive_method_raises(self):
        new_car = Car("Make", "model", 10, 100)
        new_car.refuel(10)
        with self.assertRaises(Exception) as ex:
            new_car.drive(500)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))



if __name__ == '__main__':
    main()
