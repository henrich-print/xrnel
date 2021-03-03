import sys
import os
from colored import fg

class Main:
	def __init__(self, app_self):
		self.app_self = app_self

	def build(self):
		self.clear()
		self.line()
		
		print(" MY APPS: {}{}".format(" " * 39, len(os.listdir("app"))))

		for app in os.listdir("app"):
			with open("app/{}/icon.txt".format(app), "r") as f:
				self.line()
				print(" {}{}{}\n".format(fg("yellow"), app, fg("white")))
				print(f.read())
				print("")
		key = input("[INPUT] App to run: ")
		
		if key == "q":
			os.system("reset")
			exit()

		self.run_app(app_name = key)
                

	def line(self):
		print("{}{}{}".format(fg("green"), "-" * 50, fg("white")))

	def run_app(self, app_name):
		self.clear()
		os.system("python3 app/{}/main.py".format(app_name))
		print("\n[OUTPUT] App quit.")
		input("[INPUT] Press enter to escape.")
		self.clear()

		self.build()

	def clear(self):
		os.system("clear")

def run(app_self):
	main = Main(app_self)
	main.build()
	return "menu"
