import os

def print_configuration_options():
    print('SendToFolder settings:')
    print('"ignored_path_names" - regex or directories the application won\'t include. Mostly for security reasons.')
    print('Regex or path. \n')
    print('"nested_folders" - Whether or not the application includes folders which have other folders inside of it.')
    print('0 - false, 1 - true. \n')
    print('"maximum_file_size" - Maximum file size the application accepts.')
    print('0 - no maximum, any int in megabytes. \n')
    print('"maximum_folder_size" - Maximum folder size the application accepts.')
    print('0 - no maximum, any int in megabytes. \n')
    print('Input exit to stop configuration.')


def configure():
    print_configuration_options()
    answer = ''
    while answer != 'exit':
        answer = input('Setting to configure: ')
        if answer == 'ignored_path_names':
            print('to be implemented')
        elif answer == 'nested_folders':
            print('to be implemented')
        elif answer == 'maximum_file_size':
            print('to be implemented')
        elif answer == 'maximum_folder_size':
            print('to be implemented')
        elif answer == 'help':
            print_configuration_options()
