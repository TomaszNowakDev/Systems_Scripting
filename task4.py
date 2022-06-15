import os
import shutil
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


# define main
def main():
    print("\n\tWelcome to the program\n")
    # Getting input from user, casting to string and storing in variable folder_name
    folder_name = str(input(f"How do you want to name your folder? "))
    # Calling function that takes 1 parameter name of the folder to create
    create_structure(folder_name)
    # Calling function rename_files() to rename files in the doc folder
    rename_files()


if __name__ == '__main__':
    main()
