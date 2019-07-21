PEOPLE= ('alice', 'bob')
WEEK = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')


def get_assignments():
    result = {}
    for day in WEEK:
        result[day] = {'pr': PEOPLE[0], 'webhelp': PEOPLE[1]}
    return result
