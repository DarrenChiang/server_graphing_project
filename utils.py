import os
import datetime

path = 'data/'

# Get file path based on specifications
def get_file_path(specs):
    try:
        tool = str(specs['tool'])
        chamber = str(specs['chamber'])
        year = str(specs['year'])
        month = str(specs['month']).zfill(2)
        day = str(specs['day']).zfill(2)
    except KeyError as e:
        raise ValueError(str(e) + ' is not given in the specifications.')

    return path + tool + '/' + chamber + '/' + year + '/' + month + '/' + day + '.csv'

# Get most specific path based on specifications
def get_path(specs):
    path_name = path

    if 'tool' in specs:
        path_name += str(specs['tool'])

        if 'chamber' in specs:
            path_name += '/' + str(specs['chamber'])

            if 'year' in specs:
                path_name += '/' + str(specs['year'])

                if 'month' in specs:
                    path_name += '/' + str(specs['month']).zfill(2)

    return path_name

# Parses the input string into dict
def parse_str(input_str):
    str_list = input_str.split(',')

    if len(str_list) != 5:
        raise ValueError('Input string does not follow the {tool,chamber,date,time,value} format.')

    date = parse_date(str_list[2])
    time_list = [int(float(i)) for i in str_list[3].split(':')]
    datetime.time(time_list[0], time_list[1], time_list[2])

    data = {'tool': str_list[0],
            'chamber': str_list[1],
            'time': str_list[3],
            'value': str_list[4]}

    data.update(date)

    return data

# Parses the date string into dict
def parse_date(date_str):
    try:
        date_list = [int(x) for x in date_str.split('-')]
    except:
        raise ValueError('Date string is invalid (year-month-day required)')

    datetime.datetime(date_list[0], date_list[1], date_list[2])
    return {'month': date_list[1],
            'day': date_list[2],
            'year': date_list[0]}

# Creates directory for data and returns path
def set_dir(specs, file=True):
    path_to = get_path(specs)

    if not os.path.isdir(path_to):
        os.makedirs(path_to)

    if file:
        return path_to + '/' + str(specs['day']).zfill(2) + '.csv'

    return path_to

def dummy():
    return parse_str(dummy_str())

def dummy_str():
    import random as rand
    tl = str(datetime.datetime.now()).split(' ')
    return 'tool1,chamber4,' + tl[0] + ',' + tl[1] + ',' + str(rand.randint(0, 100))
