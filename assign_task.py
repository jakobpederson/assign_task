import random

PEOPLE = ('alice', 'bob', 'cat', 'dave')
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
    pr_pool = random.sample([PEOPLE, JUNIOR], 1)[0]
    webhelp_pool = PEOPLE if pr_pool != PEOPLE else JUNIOR
    pr_excluded = [x for x in pr_pool if x not in exclude]
    webhelp_excluded = [x for x in webhelp_pool if x not in exclude]
    return (random.sample(pr_excluded, 1)[0], random.sample(webhelp_excluded, 1)[0])

def compare_days(previous_group, group):
    result = group
    if previous_group:
        pr = group[0] if group[0] != previous_group[0] else get_people([group[0]], number=1)[0]
        webhelp = group[1] if group[1] != previous_group[1] else get_people([group[1]], number=1)[0]
        if pr == webhelp:
            webhelp = get_people([webhelp, previous_group[1]], number=1)[0]
        result = [pr, webhelp]
    return result


def get_team():
    pass
