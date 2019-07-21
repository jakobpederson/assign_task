import random

PEOPLE = ('alice', 'bob', 'cat', 'dave', 'edgar', 'frank', 'greg')
JUNIOR = ('edgar', 'frank', 'greg')
WEEK = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')


def get_assignments():
    result = {}
    previous_day =[]
    for day in WEEK:
        people = get_people()
        selection = compare_days(previous_day, people)
        result[day] = {'pr': selection[0], 'webhelp': selection[1]}
        previous_day = people
    return result

def get_people(exclude=None, number=2):
    exclude = exclude or []
    selection_pool = PEOPLE
    pool = [x for x in PEOPLE if x not in exclude]
    result = random.sample(pool, number)
    return result

def compare_days(previous_group, group):
    result = group
    if previous_group:
        pr = group[0] if group[0] != previous_group[0] else get_people([group[0]], number=1)[0]
        webhelp = group[1] if group[1] != previous_group[1] else get_people([group[1]], number=1)[0]
        if pr == webhelp:
            webhelp = get_people([webhelp, previous_group[1]], number=1)[0]
        result = [pr, webhelp]
    return result

def invalid_pair(pair):
    if pair[0] in JUNIOR and pair[1] in JUNIOR:
        return True
