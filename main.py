import os
import threading
from flask import Flask

app = Flask(__name__)


def update_system():
	os.system("curl -o save.zip https://codeload.github.com/CodeDude404/RasberryPiOSIdea/zip/refs/heads/master")
	os.system("unzip save.zip")
	os.system("mv -f RasberryPiOSIdea-master/* ./")
	os.system("rm -rf RasberryPiOSIdea-master/")

@app.route('/')
def index():
	return '<a href="system/update">open update thingy</a>'


@app.route('/system/update')
def update():
	update_system()
	return 'Updating System...'
	print("updating")
	# curl -o hello.zip ftp://speedtest.tele2.net/1MB.zip


if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')