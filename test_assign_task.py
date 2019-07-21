import mock
import random
from unittest import TestCase
from assign_task import get_assignments, get_people, compare_days


class AssignTest(TestCase):

    def setUp(self):
        random.seed(5)

    def test_assign_people_to_tasks_for_each_day(self):
        result = get_assignments()
        expected = {
            'monday': {'pr': 'cat', 'webhelp': 'dave'},
            'tuesday': {'pr': 'dave', 'webhelp': 'cat'},
            'wednesday' : {'pr': 'alice', 'webhelp': 'bob'},
            'thursday': {'pr': 'bob', 'webhelp': 'cat'},
            'friday': {'pr': 'alice', 'webhelp': 'dave'}
        }
        self.assertEqual(result, expected)

    def test_randomly_select_two_people(self):
        result = get_people()
        self.assertCountEqual(result, ['cat', 'dave'])

    def test_randomly_select_people_excluding_specific_people(self):
        result = get_people(['cat', 'dave'])
        self.assertEqual(result, ['bob', 'alice'])

    def test_compare_two_groups_and_reselect_if_a_person_has_the_same_position_in_both(self):
        previous_group = ['alice', 'bob']
        group = ['alice', 'dave']
        result = compare_days(previous_group, group)
        self.assertEqual(result, ['dave', 'cat'])

    def test_compare_two_groups_and_reselect_if_both_people_have_already_had_those_positions(self):
        previous_group = ['alice', 'bob']
        group = ['alice', 'bob']
        result = compare_days(previous_group, group)
        self.assertEqual(result, ['dave', 'cat'])

    def test_two_positions_cannot_be_held_by_the_same_person(self):
        previous_group = ['dave', 'bob']
        group = ['dave', 'bob']
        result = compare_days(previous_group, group)
        self.assertEqual(result, ['cat', 'dave'])
