# next feature to add : https://www.geeksforgeeks.org/python-os-path-join-method/

import os


def welcome():
    quit = False
    print('Welcome to FileCleaner')
    command = input('If you want to begin type: DELETE\nOtherwise type: STOP ').lower()
    path_of_file = input('Choose the location of the file you want to remove: ')
    if command == 'stop':
        quit = True

    while True:

        is_exist_location = os.path.exists(path_of_file)
        if is_exist_location:
            print('%s' % path_of_file)
            file = input('Choose a file to be removed: ')
            is_exist_file = os.path.exists(file)
            if command == 'STOP':
                quit = True
                break
            if is_exist_file:
                if command == 'STOP':
                    quit = True
                    break
                path = os.path.join(path_of_file, file)
                sure = input('Are you sure you want to delete this file? (Y/N): ').lower()
                if sure == 'y':
                    os.remove(path)
                    print("%s has been removed successfully" % file)
                    command = input('Do you want to proceed?\nIf yes type: DELETE\nOtherwise: STOP ').lower()
                    if command == 'STOP':
                        quit = True
                        break
            else:
                print('There is no such file please try again!')
                continue


        else:
            path_of_file = input("This path doesn't exist.\n Please choose a valid path: ")
        if quit:
            print('Thank you for using my little program')
            print('Made by Borislav')


welcome()
#

# path = os.path.join(path_of_file, file)
#
# os.remove(path)
# print("%s has been removed successfully" % file)
