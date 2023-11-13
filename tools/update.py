import os
import sys
from time import sleep
from zipfile import ZipFile

import requests


class Update():
    def __init__(self):
        self.version = '2.6.0'
        self.github = 'https://raw.githubusercontent.com/Entity378/Bone-Skewer-Grabber-V2/main/tools/update.py'
        self.zipfile = 'https://codeload.github.com/Entity378/Bone-Skewer-Grabber-V2/zip/refs/heads/main'
        self.update_checker()

    def update_checker(self):
        code = requests.get(self.github).text
        if "self.version = '2.0'" in code:
            print('This version is up to date!')
            sleep(1)
            print('You can now open builder.pyw to open the builder!')
            sleep(1)
            print('Exiting...')
            sleep(2)
            sys.exit()
        else:
            print('''
                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                                      Your version of Bone Skewer Grabber V2 is outdated!''')
            choice = input('\nWould you like to update? (y/n): ')
            if choice.lower() == 'y':
                new_version_source = requests.get(self.zipfile)
                with open("Luna-Grabber-V2-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Bone-Skewer-Grabber-V2-main.zip", 'r') as filezip:
                    filezip.extractall(path=os.path.join(os.path.expanduser("~"), "Desktop"))
                os.remove("Bone-Skewer-Grabber-V2-main.zip")
                print('The new version is now on your desktop.\nUpdate Complete!')
                print("Exiting...")
                sleep(5)
            if choice.lower() == 'n':
                print('Exiting...')
                sleep(2)
                sys.exit()


if __name__ == '__main__':
    Update()
