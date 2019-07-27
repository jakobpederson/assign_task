import random

WEEK = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
JOBS = ('pr', 'webhelp')


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

def get_week(first, second):
    result = {day: {} for day in WEEK}
    for day in WEEK:
        people = get_people(first, second)
        jobs = assign_job(people)
        for val in JOBS:
            result[day].update({
                val: {
                    'person': jobs[val]['person'],
                    'source': jobs[val]['source'],
                },
            })
    result = compare_jobs(result)
    return result

def compare_jobs(result):
    compare = WEEK[0]
    for day, value in result.items():
        if day != compare:
            result = update_repeating_jobs(value, result[compare], result)
        compare = day
    return result

def update_repeating_jobs(value, compare, result):
    for val in :
        job_1 = value[val]
        job_2 = compare[val]
        if job_1['person'] == job_2['person']:
            job_1['person'] = random.sample(job_1['source'], 1)[0]
    return result
