#This is the main python file.
#Please do not touch unless your are ABSOLUTELY SURE ABOUT WHAT YOU ARE DOING
#Thanks :)

#export FLASK_APP=mainpythonfile.py
#python -m flask run

import pickle
import os, sys

from flask import *
app = Flask(__name__)

message = ""
number = 0

# Load all users according to "users.p" and display their stats

MY_DIR  = os.path.realpath(os.path.dirname(__file__))
PICKLE_DIR = os.path.join(MY_DIR, 'data')

USERS = "users.p"
USERSPATH = os.path.join(PICKLE_DIR, USERS)

users = []

#Load users from their .p files
with open(USERSPATH, 'rb') as f:
    usersArray = pickle.load(f)

for file in usersArray:
    fname = os.path.join(PICKLE_DIR, file)
    print("Opening " + str(fname))
    with open(fname, 'rb') as f:
        peps = pickle.load(f)
        users.append(peps)


#All app.route functions
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loginuser', methods=['POST'])
def calcmessage():
    username = request.form['username']
    print("Logging in to " + str(username))
    return redirect(url_for('user', name=username))

@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    for person in users:
        if name == person.name:
            return render_template('finances.html', money=person.money, netIncome=person.netIncome, income=person.income,
                                   expenses=person.expenses, netWorth=person.netWorth)
    return "Invaild username"

#Button example ---------------#
#@app.route('/button')
#def button():
#    return render_template('button.html', message=message, number=number)

#@app.route('/calcmessage', methods=['POST'])
#def calcmessage():
#    global message
#    message = request.form['message']
#    print(request.form['message'])
#    return redirect(url_for('button'))

#@app.route('/addone', methods=['POST'])
#def addone():
#    global number
#    if request.form['add1']:
#        number += 1
#    print(number)
#    return redirect(url_for('button'))
#Button example ---------------#

if __name__ == "__main__":
    app.run()