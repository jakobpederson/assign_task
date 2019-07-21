PEOPLE= ('alice', 'bob')
WEEK = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')


def get_assignments():
    result = {}
    for day in WEEK:
        result[day] = PEOPLE
    return result
