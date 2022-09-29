from unittest import TestCase, main
from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("username", 1, 100, 55)

    def test_constructor(self):
        username = self.hero.username
        level = self.hero.level
        health_points = self.hero.health
        damage = self.hero.damage

        self.assertEqual("username", username)
        self.assertEqual(1, level)
        self.assertEqual(100, health_points)
        self.assertEqual(55, damage)

    def test_battle_method_the_happy_case(self):
        other_hero = Hero("Other username", 1, 50, 50)

        result = self.hero.battle(other_hero)

        self.assertEqual(55, self.hero.health)
        self.assertEqual(-5, other_hero.health)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(60, self.hero.damage)

        expected = "You win"
        self.assertEqual(expected, result)

    def test_battle_method_same_hero_username_exception(self):
        other_hero = Hero("username", 1, 75, 50)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(other_hero)

        expected = "You cannot fight yourself"
        self.assertEqual(expected, str(ex.exception))

    def test_battle_method_lower_or_equal_to_zero_health_exception(self):
        other_hero = Hero("other hero", 1, 0, 50)
        this_hero = Hero("this hero", 1, 10, 43)

        with self.assertRaises(Exception) as ex:
            other_hero.battle(this_hero)

        expected = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected, str(ex.exception))

    def test_battle_method_lower_or_equal_to_zero_health_for_opponent_exception(self):
        other_hero = Hero("other hero", 1, 12, 50)
        this_hero = Hero("this hero", 1, 0, 43)

        with self.assertRaises(Exception) as ex:
            other_hero.battle(this_hero)

        expected = f"You cannot fight {this_hero.username}. He needs to rest"
        self.assertEqual(expected, str(ex.exception))

    def test_battle_method_draw_case(self):
        other_hero = Hero("other hero", 2, 100, 100)
        this_hero = Hero("this hero", 2, 100, 100)
        result = this_hero.battle(other_hero)

        expected = "Draw"
        self.assertEqual(expected, result)

    def test_battle_method_lose_case(self):
        other_hero = Hero("other hero", 2, 100, 100)
        result = self.hero.battle(other_hero)

        expected = "You lose"
        self.assertEqual(3, other_hero.level)
        self.assertEqual(50, other_hero.health)
        self.assertEqual(105, other_hero.damage)

        self.assertEqual(expected, result)

    def test_the_dunder_str_method(self):
        result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(result, str(self.hero))
