import mock
import random
from unittest import TestCase
from assign_task import get_people, assign_job, get_week

FIRST = ['a', 'b', 'c']
SECOND = ['d', 'e', 'f']


class AssignTest(TestCase):

    def setUp(self):
        random.seed(5)

    def test_take_one_person_from_each_list(self):
        result = get_people(FIRST, SECOND)
        self.assertEqual(result['c'], [x for x in FIRST if x != 'c'])
        self.assertEqual(result['e'], [x for x in SECOND if x != 'e'])

    def test_assign_job(self):
        people = get_people(FIRST, SECOND)
        result = assign_job(people)
        self.assertEqual(result['pr'], {'person': 'e', 'source': ['d', 'f']})
        self.assertEqual(result['webhelp'], {'person': 'c', 'source': ['a', 'b']})

    def test_assign_jobs_for_each_day_in_a_week(self):
        result = get_week(FIRST, SECOND)
        expected = {
            'monday': {
                'pr': {'person': 'e', 'source': ['d', 'f']},
                'webhelp': {'person': 'c', 'source': ['a', 'b']}
            },
            'tuesday': {
                'pr': {'person': 'c', 'source': ['a', 'b']},
                'webhelp': {'person': 'f', 'source': ['d', 'e']}
            },
            'wednesday': {
                'pr': {'person': 'b', 'source': ['a', 'c']},
                'webhelp': {'person': 'd', 'source': ['e', 'f']}
            },
            'thursday': {
                'pr': {'person': 'd', 'source': ['e', 'f']},
                'webhelp': {'person': 'a', 'source': ['b', 'c']}
            },
            'friday': {
                'pr': {'person': 'e', 'source': ['e', 'f']},
                'webhelp': {'person': 'b', 'source': ['a', 'c']}
            }
        }
        self.assertEqual(result, expected)

    def test_people_cannot_do_same_job_two_days_in_a_row(self):
        result = get_week(FIRST, SECOND)
        self.assertNotEqual(
            result['monday']['pr']['person'],
            result['tuesday']['pr']['person']
        )
        self.assertNotEqual(
            result['monday']['webhelp']['person'],
            result['tuesday']['webhelp']['person']
        )
        self.assertNotEqual(
            result['tuesday']['pr']['person'],
            result['wednesday']['pr']['person'],
        )
        self.assertNotEqual(
            result['tuesday']['webhelp']['person'],
            result['wednesday']['webhelp']['person'],
        )
        self.assertNotEqual(
            result['wednesday']['pr']['person'],
            result['thursday']['pr']['person'],
        )
        self.assertNotEqual(
            result['wednesday']['webhelp']['person'],
            result['thursday']['webhelp']['person'],
        )
        self.assertNotEqual(
            result['thursday']['pr']['person'],
            result['friday']['pr']['person'],
        )
        self.assertNotEqual(
            result['thursday']['webhelp']['person'],
            result['friday']['webhelp']['person'],
        )
