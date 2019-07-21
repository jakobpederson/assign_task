from unittest import TestCase
from assign_task import get_assignments


class AssignTest(TestCase):

    def test_x(self):
        result = get_assignments()
        expected = {
            'monday': ('alice', 'bob')
        }
        self.assertEqual(result, expected)
        self.fail('x')

    def test_2(self):
        result = get_assignments()
        expected = {
            'monday': ('alice', 'bob')
            'tuesday': ('alice', 'bob')
            'wednesday': ('alice', 'bob')
            'thursday': ('alice', 'bob')
            'friday': ('alice', 'bob')
        }
        self.assertEqual(result, expected)
        self.fail('x')
