import random
from unittest import TestCase
from assign_task import get_assignments, get_two


class AssignTest(TestCase):

    def test_x(self):
        result = get_assignments()
        expected = {
            'monday': {'pr': 'alice', 'webhelp': 'bob'},
            'tuesday': {'pr': 'alice', 'webhelp': 'bob'},
            'wednesday': {'pr': 'alice', 'webhelp': 'bob'},
            'thursday': {'pr': 'alice', 'webhelp': 'bob'},
            'friday': {'pr': 'alice', 'webhelp': 'bob'},
        }
        self.assertEqual(result, expected)
        self.fail('x')

    def test_y(self):
        random.seed(5)
        result = get_two()
        self.assertCountEqual(result, ('cat', 'dave'))
