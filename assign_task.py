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

def compare_days(previous_group, group):
    pr = group[0] if group[0] != previous_group[0] else get_people(group, number=1)[0]
    webhelp = group[1] if group[1] != previous_group[1] else get_people(group, number=1)[0]
    return [pr, webhelp]
