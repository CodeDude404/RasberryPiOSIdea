import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def update():
    return '<a href="system/update">open update thingy</a>'


@app.route('/system/update')
def update():
    return 'Updating System...'
	os.system("curl https://github.com/CodeDude404/RasberryPiOSIdea/archive/refs/heads/master.zip >> output.zip")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')