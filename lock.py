from datetime import datetime
from colored import fg

def run(app_self):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print("\n" * 20)
    print("{}{}{}{}{}".format(fg("green"), " " * 21, current_time, " " * 21, fg("white")))
    print("\n" * 20)

    password = input(" {}[INPUT] Password: {}".format(fg("red"), fg("white")))
    if ":" in password:
        password, special = password.split(":")
    else:
        special = "all"

    if password == app_self.usr["password"]:
        if special == "all":
            return "menu"
        elif special == "prwt":
            return "menu_prwt"
    else:
        return "lock"
