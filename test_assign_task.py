import random
from unittest import TestCase
from assign_task import get_assignments, get_two


class AssignTest(TestCase):

    def setUp(self):
        random.seed(5)

    def test_x(self):
        result = get_assignments()
        expected = {
            'monday': {'pr': 'cat', 'webhelp': 'dave'},
            'tuesday': {'pr': 'cat', 'webhelp': 'dave'},
            'wednesday': {'pr': 'alice', 'webhelp': 'bob'},
            'thursday': {'pr': 'bob', 'webhelp': 'cat'},
            'friday': {'pr': 'alice', 'webhelp': 'dave'}
        }
        self.assertEqual(result, expected)

    def test_y(self):
        result = get_two()
        self.assertCountEqual(result, ('cat', 'dave'))
