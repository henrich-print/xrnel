import os
from colored import fg, bg
import lock, menu, menu_prwt #horible but whotever :)

def line(index = "-", color = "red", width = 50):
	print("{}{}{}".format(fg(color), index * 50, fg("white")))

def clear():
	os.system("clear")

def load_json(file_path):
	with open(file_path, "r") as f:
		return eval(f.read())

class Main:
	def __init__(self):
		self.usr = load_json("data/usr.json")

		self.open_screen = "lock"

	def build(self):
		clear()
		self.open_screen = eval("{}.run".format(self.open_screen))(self)
		self.build()

if __name__ == '__main__':
	main = Main()
	main.build()
