from unittest import TestCase, main
from project.team import Team


class TeamTest(TestCase):
    def setUp(self) -> None:
        self.team = Team("Bulgarians")

    def test_constructor(self):
        self.assertEqual("Bulgarians", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_attribute_with_numbers_and_other_symbols_input(self):
        with self.assertRaises(ValueError) as ve:
            team = Team("124")
        expected = "Team Name can contain only letters!"
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            team = Team("./,!@#%$^")
        self.assertEqual(expected, str(ve.exception))

    def test_add_member_method(self):
        result = self.team.add_member(Ivaylo=17, Emin=16)
        expected = {'Ivaylo': 17, 'Emin': 16}
        self.assertEqual(expected, self.team.members)

        expected = "Successfully added: Ivaylo, Emin"
        self.assertEqual(expected, result)

    def test_remove_name_method_with_existing_name(self):
        self.team.add_member(Ivaylo=17, Emin=16)
        result = self.team.remove_member("Ivaylo")
        expected = {'Emin': 16}
        self.assertEqual(expected, self.team.members)

        expected = "Member Ivaylo removed"
        self.assertEqual(expected, result)

    def test_remove_name_method_with_non_existing_name(self):
        self.team.add_member(Ivaylo=17, Emin=16)
        result = self.team.remove_member("Name")
        expected = "Member with name Name does not exist"
        self.assertEqual(expected, result)

    def test_greater_than_method_with_true_output(self):
        other_team = Team("Barbarians")
        self.team.add_member(Ivaylo=17, Emin=16)
        other_team.add_member(barbarian=15)
        result = self.team > other_team
        self.assertEqual(True, result)

    def test_greater_than_method_with_false_output(self):
        other_team = Team("Barbarians")
        self.team.add_member(Ivaylo=17, Emin=16)
        other_team.add_member(barbarian=15, barbarian2=19)
        result = self.team > other_team
        self.assertEqual(False, result)

        other_team.add_member(barbarian3=21)
        result = self.team > other_team
        self.assertFalse(result)

    def test_the_len_method(self):
        self.team.add_member(Ivaylo=17, Emin=16)
        result = len(self.team)
        expected = 2

        self.assertEqual(expected, result)

    def test_the_add_method(self):
        other_team = Team("Barbarians")
        self.team.add_member(Ivaylo=17, Emin=16)
        other_team.add_member(barbarian=15, barbarian2=19)
        new_team = self.team + other_team

        name = "BulgariansBarbarians"
        members = {"Ivaylo": 17, "Emin": 16, "barbarian": 15, "barbarian2": 19}
        self.assertEqual(name, new_team.name)
        self.assertEqual(members, new_team.members)

    def test_the_str_method(self):
        other_team = Team("Barbarians")
        other_team.add_member(barbarian=15, barbarian2=19)

        expected = f"Team name: Barbarians\nMember: barbarian2 - 19-years old\nMember: barbarian - 15-years old"
        result = str(other_team)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()