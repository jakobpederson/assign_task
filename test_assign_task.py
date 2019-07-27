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
            'monday': {'pr': 'e', 'webhelp': 'c'},
            'tuesday': {'pr': 'c', 'webhelp': 'f'},
            'wednesday': {'pr': 'b', 'webhelp': 'd'},
            'thursday': {'pr': 'd', 'webhelp': 'a'},
            'friday': {'pr': 'd', 'webhelp': 'b'},
        }
        self.assertEqual(result['monday']['pr']['person'], expected['monday']['pr'])
        self.assertEqual(result['monday']['webhelp']['person'], expected['monday']['webhelp'])
        self.assertEqual(result['tuesday']['pr']['person'], expected['tuesday']['pr'])
        self.assertEqual(result['tuesday']['webhelp']['person'], expected['tuesday']['webhelp'])
        self.assertEqual(result['wednesday']['pr']['person'], expected['wednesday']['pr'])
        self.assertEqual(result['wednesday']['webhelp']['person'], expected['wednesday']['webhelp'])
        self.assertEqual(result['thursday']['pr']['person'], expected['thursday']['pr'])
        self.assertEqual(result['thursday']['webhelp']['person'], expected['thursday']['webhelp'])
        self.assertEqual(result['friday']['pr']['person'], expected['friday']['pr'])
        self.assertEqual(result['friday']['webhelp']['person'], expected['friday']['webhelp'])

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
