import os
import threading
from flask import Flask

app = Flask(__name__)


def update_system():
	os.system("curl -o save.zip https://codeload.github.com/CodeDude404/RasberryPiOSIdea/zip/refs/heads/master")
	os.system("unzip save.zip")
	os.system("mv RasberryPiOSIdea-master/* ./")

@app.route('/')
def index():
	return '<a href="system/update">open update thingy</a>'


@app.route('/system/update')
def update():
	print("updating")
	# curl -o hello.zip ftp://speedtest.tele2.net/1MB.zip
	update_system()
	return 'Updating System...'


if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')