from flask import Flask,render_template,request,session,redirect, url_for
import pymongo
from pymongo import MongoClient

import os
import socket


#define flask app
app=Flask(__name__)
client=MongoClient("mongodb://Ash:kneelbeforeme@localhost:27017/ERecDB")
db=client["ERecDB"]

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/',methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		auc=db["authentication"]
		user=auc.find_one({"username":request.form['username']})
		print(user)
		if(user!=None) :
			if(request.form['password']==user["passwd"]):
				return(redirect(url_for('index')))
			else:
				error = "Invalid password"
		else:
			error = "Invalid username"		
	return(render_template('login.html',error=error))

if __name__ == '__main__':
	app.config['DEBUG'] = True #helps you to see changes without re-running app
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 0))
	port = sock.getsockname()[1]
	sock.close()
	app.run(port=port)