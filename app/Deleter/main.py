import os

def get_path():
    path = os.path.abspath(__file__)
    return path.replace("app/Deleter/main.py", "")

class Main:
    def __init__(self):
        self.app_name = input("[INPUT] App name: ")
        self.path = get_path()

    def remove(self):
        os.system("rm -r {}/app/{}".format(self.path, self.app_name))

main = Main()
main.remove()
        
