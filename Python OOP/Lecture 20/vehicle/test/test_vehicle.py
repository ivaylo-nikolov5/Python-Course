from unittest import TestCase, main
from vehicle.project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(20, 150)

    def test_constructor(self):
        self.assertEqual(20, self.vehicle.fuel)
        self.assertEqual(20, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method(self):
        self.vehicle.drive(4)
        self.assertEqual(15, self.vehicle.fuel)

    def test_if_drive_method_raises(self):
        expected = "Not enough fuel"
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(40)
        self.assertEqual(expected, str(ex.exception))

    def test_refuel_method(self):
        self.vehicle.drive(4)
        self.vehicle.refuel(5)
        self.assertEqual(20, self.vehicle.fuel)

    def test_if_refuel_method_raises(self):
        expected = "Too much fuel"
        self.vehicle.drive(4)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual(expected, str(ex.exception))

    def test_str_method(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        result = str(self.vehicle)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()

