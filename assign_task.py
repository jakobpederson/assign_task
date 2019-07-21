import random

PEOPLE= ('alice', 'bob', 'cat', 'dave')
WEEK = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')


def get_assignments():
    result = {}
    for day in WEEK:
        people = get_two()
        result[day] = {'pr': people[0], 'webhelp': people[1]}
    return result

def get_two():
    two  = random.sample(PEOPLE, 2)
    return two
