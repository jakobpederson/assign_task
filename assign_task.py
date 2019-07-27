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

def get_people(first, second):
    select_1 = random.sample(first, 1)[0]
    select_2 = random.sample(second, 1)[0]
    return {
        select_1: [person for person in first if person != select_1],
        select_2: [person for person in second if person != select_2]
    }

def assign_job(people):
    keys = list(people.keys())
    pr = random.sample(keys, 1)[0]
    webhelp = keys[0] if pr != keys[0] else keys[1]
    return {
        'pr': {'person': pr, 'source': people[pr]},
        'webhelp': {'person': webhelp, 'source': people[webhelp]},
    }

def compare_days(previous_group, group):
    result = group
    if previous_group:
        pr = group[0] if group[0] != previous_group[0] else get_people([group[0]], number=1)[0]
        webhelp = group[1] if group[1] != previous_group[1] else get_people([group[1]], number=1)[0]
        if pr == webhelp:
            webhelp = get_people([webhelp, previous_group[1]], number=1)[0]
        result = [pr, webhelp]
    return result

def get_week(first, second):
    pass
    # result = {}
    # test_day = WEEK[0]
    # for day in WEEK:
    #     people = get_people(first, second)
    #     jobs = assign_job(people)
    #     if test_day != day:
    #         if test_day['pr'] == jobs['pr']:
    #     result[day] = jobs
    # return result

