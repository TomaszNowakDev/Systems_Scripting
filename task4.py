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


# define main
def main():
    print("\n\tWelcome to the program\n")
    # Getting input from user, casting to string and storing in variable folder_name
    folder_name = str(input(f"How do you want to name your folder? "))
    # Calling function that takes 1 parameter name of the folder to create
    create_structure(folder_name)


if __name__ == '__main__':
    main()
