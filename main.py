import os
import shutil

PATH = input('Enter full path to directory that will be sorted: ')

# <----------------------- Funcions ----------------------->
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def make_dir(dir_name):
    folder = dir_name[1:].upper() + '_Files'
    full_path = PATH + folder + '/'
    if not os.path.isdir(full_path):
        os.mkdir(full_path)
    return full_path

def move_files(list_of_files):
    for file in list_of_files:
        file_name, extension = os.path.splitext(file)
        new_path = make_dir(extension)
        shutil.move(PATH + file, new_path + file)
# <----------------------- Funcions ----------------------->

list_of_files = []
if os.path.exists(PATH):
    for file in files(PATH):
        list_of_files.append(file)
else:
    print('Invalid directory specified.')
        
if __name__ == '__main__':
    move_files(list_of_files)
