import os
import shutil
import zipfile
from os.path import isdir

# define main_folder variable later on I will make it global to facilitate access to the path of the folder
main_folder = ''


def create_structure(fname):
    current_folder = os.getcwd()  # get current directory
    folder_exists = isdir(os.path.join(os.sep, current_folder, fname))
    # check if folder exists
    if folder_exists:
        print('This folder already exists, I delete it before starting the operation...\n')
        # if folder exists remove it and all of the content
        shutil.rmtree(os.path.join(os.sep, current_folder, fname))
    else:
        print('Creating new folders structure...\n')

    # now create new structure of folders
    global main_folder  # make main_folder a global variable
    main_folder = os.path.join(os.sep, current_folder, fname)  # assign value to main_folder
    # make folders required for specification
    os.makedirs(os.path.join(os.sep, main_folder, 'backup'))
    os.makedirs(os.path.join(os.sep, main_folder, 'working', 'pics'))
    os.makedirs(os.path.join(os.sep, main_folder, 'working', 'movie'))
    os.makedirs(os.path.join(os.sep, main_folder, 'working', 'docs', 'party'))
    os.makedirs(os.path.join(os.sep, main_folder, 'working', 'docs', 'school'))

    # change of current working directory to docs
    os.chdir(os.path.join(os.sep, main_folder, 'working', 'docs'))
    # make list of files_names
    files_names = ['CORONAVIRUS.txt', 'DANGEROUS.txt', 'KEEPSAFE.txt', 'STAYHOME.txt', 'HYGIENE.txt']
    # loop through list of files
    for i, value in enumerate(files_names):
        f = open(value, 'w')  # establish connection to file in write mode
        f.write(f"This is the name of the {files_names[i]} file before changing name.")  # write to file
        f.close()  # close connection to file
    print('...new folders created successfully!')


# Function definition
def rename_files():
    print("Renaming files in progress...\n")
    # check if folder exists
    folder_exists = isdir(os.path.join(os.sep, main_folder, 'working', 'docs'))
    if folder_exists:
        # change the name of all .txt files
        for file in os.listdir(os.path.join(os.sep, main_folder, 'working', 'docs')):
            if file.endswith('.txt'):
                # Use lowercase for chars from start to last 3 chars in word and use uppercase for last 3 chars
                os.rename(file, file[:-3].lower() + file[-3:].upper())
    print('...files renamed successfully!')


# Function definition
def make_a_backup():
    print('Preparing for backup...\n')
    # change of current working directory to working
    os.chdir(os.path.join(os.sep, main_folder, 'working'))
    # coping and moving folder 'docs' to backup
    shutil.copytree(os.path.join(os.sep, main_folder, 'working', 'docs'),
                    os.path.join(os.sep, main_folder, 'backup', 'docs'))

    # change of current working directory to backup
    os.chdir(os.path.join(os.sep, main_folder, 'backup'))
    new_zip = zipfile.ZipFile('backup1.zip', 'w')  # create backup1.up in writing mode
    # walking through the folder and zipping elements
    for foldername, subfolders, filenames in os.walk('docs'):
        new_zip.write(foldername)
        for filename in filenames:
            new_zip.write(os.path.join(foldername, filename))  # write to new_zip

    new_zip.close()  # close new_zip
    # making 7 copies of backup file and call them consecutive numbers
    for i in range(6):
        shutil.copy(os.path.join(os.sep, main_folder, 'backup', 'backup1.zip'), os.path.join(os.sep, main_folder, 'backup', f"backup{i + 2}.zip"))

    # remove additional copy of doc folder in backup folder
    shutil.rmtree(os.path.join(os.sep, main_folder, 'backup', 'docs'))
    print('...backup completed!\nContent of the backup folder is: ')
    # print list of backup folder content
    print(os.listdir(os.path.join(os.sep, main_folder, 'backup')))


# define main
def main():
    print("\n\tWelcome to the program\n")
    # Getting input from user, casting to string and storing in variable folder_name
    folder_name = str(input(f"How do you want to name your folder? "))
    # Calling function that takes 1 parameter name of the folder to create
    create_structure(folder_name)
    # Calling function rename_files() to rename files in the doc folder
    rename_files()
    # Calling function make_a_backup() to make a backup of the doc folder
    make_a_backup()


if __name__ == '__main__':
    main()
