import random

PEOPLE= ('alice', 'bob', 'cat', 'dave')
WEEK = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')


def get_assignments():
    result = {}
    for day in WEEK:
        people = get_people()
        result[day] = {'pr': people[0], 'webhelp': people[1]}
    return result

def get_people(exclude=None, number=2):
    exclude = exclude or []
    pool = [x for x in PEOPLE if x not in exclude]
    result = random.sample(pool, number)
    return result
