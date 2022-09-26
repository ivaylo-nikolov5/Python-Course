from unittest import TestCase, main


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(TestCase):
    def test_size_increase_after_eating(self):
        cat = Cat("test")
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_is_cat_fed_after_eating(self):
        cat = Cat("test")
        cat.eat()
        self.assertEqual(True, cat.fed)

    def test_fed_many_times_raise(self):
        cat = Cat("test")
        with self.assertRaises(Exception) as ex:
            cat.eat()
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_fall_asleep_without_being_fed(self):
        cat = Cat("test")
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_if_cat_is_not_sleepy_After_sleeping(self):
        cat = Cat("test")
        cat.eat()
        cat.sleep()
        self.assertEqual(False, cat.sleepy)

if __name__ == '__main__':
    main()


