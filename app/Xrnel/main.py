from flask import Flask, render_template
from threading import Timer
from os import system
from os import path as program_path

app = Flask(__name__)

def list_to_str(list_obj):
	str_list = ""
	for i in list_obj:
		str_list += "{}/".format(i)
	return str_list

def load_json(file_path):
	with open(file_path, "r") as f:
		return eval(f.read())

def load_path():
	path = program_path.abspath(__file__).split("/")
	path = path[0:path.index("Xrnel")]
	path = list_to_str(path)
	path += "Xrnel/data/path.json"
	return load_json(path)

def load_usr():
	path = program_path.abspath(__file__).split("/")
	path = path[0:path.index("Xrnel")]
	path = list_to_str(path)
	path += "Xrnel/data/usr.json"
	return load_json(path)

@app.route("/")
def home():
	return render_template("index.html")

def open():
	system("xdg-open http://127.0.0.1:5000/")

if __name__ == '__main__':
	Timer(5, open).start()
	app.run()
