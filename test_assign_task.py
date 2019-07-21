import random
from unittest import TestCase
from assign_task import get_assignments, get_people


class AssignTest(TestCase):

    def setUp(self):
        random.seed(5)

    def test_assign_people_to_tasks_for_each_day(self):
        result = get_assignments()
        expected = {
            'monday': {'pr': 'cat', 'webhelp': 'dave'},
            'tuesday': {'pr': 'cat', 'webhelp': 'dave'},
            'wednesday': {'pr': 'alice', 'webhelp': 'bob'},
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
