from utils import *
from zipfile import ZipFile as zp
from zipfile import ZIP_DEFLATED
import datetime
import shutil
import os

# Zips the data files x months ago and removes empty directories if specified
def zip_dir(months, rm=False):
    current = datetime.datetime.now()
    month = current.month
    year = current.year
    month -= months

    if month < 1:
        month = 12 + month
        year -= 1

    zip_file = str(year) + '-' + str(month) + '.zip'
    zipper = zp(zip_file, 'w', ZIP_DEFLATED)
    rm_list = list()

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.csv'):
                dir_list = root.replace(path, '').split('\\')

                if int(dir_list[2]) == year and int(dir_list[3]) == month:
                    file_path = root + '/' + file
                    zipper.write(file_path)
                    rm_list.append((file_path, root))

    zipper.close()

    if rm:
        for file_path, root in rm_list:
            os.remove(file_path)

        rm_empty_dir(path)

# Removes all directories that do not have files (will remove inner directories)
def rm_empty_dir(path):
    for f in os.listdir(path):
        f_path = path + '/' + f
        if os.path.isdir(f_path):
            rm_empty_dir(f_path)

            if len(os.listdir(f_path)) == 0:
                os.rmdir(f_path)