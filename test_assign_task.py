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
        self.assertEqual(result, expected)

    def test_people_cannot_do_same_job_two_days_in_a_row(self):
        result = get_week(FIRST, SECOND)
        self.assertTrue(result['monday']['pr'] != result['tuesday']['pr'])
        self.assertTrue(result['tuesday']['pr'] != result['tuesday']['pr'])
        self.assertTrue(result['wednesday']['pr'] != result['tuesday']['pr'])
        self.assertTrue(result['thursday']['pr'] != result['tuesday']['pr'])
        self.assertTrue(result['friday']['pr'] != result['tuesday']['pr'])
        self.assertTrue(result['monday']['webhelp'] != result['monday']['webhelp'])
        self.assertTrue(result['tuesday']['webhelp'] != result['tuesday']['webhelp'])
        self.assertTrue(result['wednesday']['webhelp'] != result['wednesay']['webhelp'])
        self.assertTrue(result['thursday']['webhelp'] != result['thursday']['webhelp'])
        self.assertTrue(result['friday']['webhelp'] != result['friday']['webhelp'])
