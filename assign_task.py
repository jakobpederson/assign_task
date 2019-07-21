import random

PEOPLE= ('alice', 'bob', 'cat', 'dave')
WEEK = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')


def get_assignments():
    result = {}
    for day in WEEK:
        result[day] = {'pr': PEOPLE[0], 'webhelp': PEOPLE[1]}
    return result

def get_two():
    two  = random.sample(PEOPLE, 2)
    return two
