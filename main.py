#import subprocess as sp
#output = sp.getoutput('pip install flask')
# print (output)


from flask import Flask

app = Flask(__name__)

@app.route('/system/update')
def update():
    return 'Updating System...'
	os.system()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')