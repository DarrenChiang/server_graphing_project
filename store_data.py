from utils import *
import sys

# Creates csv file and or appends new data entry
def store_data(data, file_path):
    with open(file_path, 'a+') as file:
        # If file is not empty, add a newline
        if file.tell() != 0:
            file.write('\n')

        file.write(str(data['time']) + ', ' + str(data['value']))

# Stores data string input into its respective csv file
def store(data_str):
    try:
        data = parse_str(data_str)
        path = set_dir(data)
        store_data(data, path)
    except ValueError as error:
        print(error)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit()

    for i in range(1, len(sys.argv)):
        input_str = sys.argv[i]
        store(input_str)