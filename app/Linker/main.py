import os

def clear():
    os.system("clear")

def get_path():
    path = os.path.abspath(__file__)
    return path.replace("app/Linker/main.py", "")

def app_code(link):
    return "from os import system\nsystem('xdg-open {}')".format(link)

class Main:
    def __init__(self):
        self.app_name = input(" [INPUT] App name: ")
        self.link = input(" [INPUT] App link: ")
        self.path = get_path()

        self.folder_path = "{}/app/{}".format(self.path, self.app_name)

    def make_app(self):
        os.mkdir(self.folder_path)

        with open("{}/main.py".format(self.folder_path), "w") as f:
                f.write(app_code(self.link))

        icon_0 = " {}".format(input(" [ICON][INPUT][0]: "))
        icon_1 = " {}".format(input(" [ICON][INPUT][1]: "))
        icon_2 = " {}".format(input(" [ICON][INPUT][2]: "))

        with open("{}/icon.txt".format(self.folder_path), "w") as f:
            f.write("{}\n{}\n{}\n".format(icon_0, icon_1, icon_2))

if __name__ == "__main__":
    main = Main()
    main.make_app()
