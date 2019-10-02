import os, sys, shutil
from configure import configure

shortcut_name = 'Folder.lnk'
SendToFolder_shortcut_path = os.path.abspath(os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\SendTo\\'))
SendToFolder_shortcut_file_path = os.path.abspath(os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\SendTo\\' + shortcut_name))
shortcut_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static\\' + shortcut_name))

def does_shortcut_exist():
    return os.path.exists(os.path.join(SendToFolder_shortcut_path, shortcut_name))

def main():
    print('SendToFolder configuration')
    if not does_shortcut_exist():
        print('SendToFolder is not installed. Do you want to install it now?')
        answer = ''
        while answer != 'y' and answer != 'n':
            answer = input('(y/n):').lower()
            if answer == 'y':
                shutil.copyfile(shortcut_path, SendToFolder_shortcut_file_path)
                if does_shortcut_exist():
                    print('Installation complete!')
                else:
                    print('Something went wrong, please try again.')
            elif answer != 'n':
                print('Please type y or n.')

    print('Do you want to configure SendToFolder settings?')
    configure()

if __name__ == '__main__':
    main()
