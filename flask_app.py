from flask import Flask,render_template,request,session,redirect, url_for
import pymongo
from pymongo import MongoClient
import os
import socket


# Get username & password to get acces to database (Replace with your file)
#filename='/home/ashik/cred.txt'
#temp=open(filename,'r').read().split('\n')

#define flask app
app=Flask(__name__)
client=MongoClient("mongodb://localhost:27017")
db=client["ERecDB"]

@app.route('/')
@app.route('/home')
def home():
	return "Welcome"
'''
@app.route('/index')
def index():
    return render_template('index.html')
  '''  
@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		auc=db["authentication"]
		user=auc.find_one({"username":request.form['username']})
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
