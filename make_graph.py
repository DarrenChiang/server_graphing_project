from utils import *
import matplotlib.pyplot as plt
import datetime

# Get data of specified tool, chamber, year, month, and day in dict
# Note: can only get unzipped data for now
def get_data(specs):
    file_path = get_file_path(specs)
    time = list()
    value = list()

    with open(file_path) as file:
        for line in file.readlines():
            x, y = line.replace(' ', '').replace('\n', '').split(',')
            t = x.split(':')
            s = t[2].split('.')
            time.append(datetime.datetime(specs['year'],
                                          specs['month'],
                                          specs['day'],
                                          hour=int(t[0]),
                                          minute=int(t[1]),
                                          second=int(s[0]),
                                          microsecond=int(s[1])))
            value.append(float(y))

    return time, value

# Graph all specifications in one graph (assuming they are of the same day)
def graph(*specs):
    for spec in specs:
        try:
            x, y = get_data(spec)
            plt.plot(x, y, label=spec['tool'] + ', ' + spec['chamber'])
        except:
            print('Data could not be retrieved from specification:')
            print(str(spec))

    plt.show()

# Identical to graph() but using a list instead of *args
def graph_list(specs):
    for spec in specs:
        try:
            x, y = get_data(spec)
            plt.plot(x, y, label=spec['tool'] + ', ' + spec['chamber'])
        except:
            print('Data could not be retrieved from specification:')
            print(str(spec))

    plt.show()

def spec():
    return {'tool': 'tool1',
            'chamber': 'chamber4',
            'year': 2020,
            'month': 6,
            'day': 11}