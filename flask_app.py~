from flask import Flask,render_template,request,session,redirect, url_for,jsonify
import pymongo
from pymongo import MongoClient
import os
import socket


# Read username & password from cred file to get acces to database (Replace with your file)
filename='/home/ashik/cred.txt'
temp=open(filename,'r').read().split('\n')

# Connecting to mongodb databse hosted at mlab
DB_NAME="erecdb"  
DB_HOST="ds043047.mlab.com"
DB_PORT=43047
DB_USER=temp[0] 
DB_PASS=temp[1]

connection = MongoClient(DB_HOST, DB_PORT)
db = connection[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

# define flask app
app=Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

# User registration page
@app.route('/')
def register():
	return render_template('register.html')
	
# User login page 	
@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		auc=db["authentication"]
		user=auc.find_one({"uname":request.form['username']})
		if(user!=None) :
			if(request.form['password']==user["passwd"]):
				return(redirect(url_for('elective')))
			else:
				error = "Invalid password"
		else:
			error = "Invalid username"					
	return(render_template('login.html',error=error))


# Elective form input page
@app.route('/elective',methods=['GET','POST'])
def elective():
	return render_template('elecFormProgressive.html')
<<<<<<< HEAD
	
@app.route('/visualisation',methods=['GET','POST'])
def visualisation():	
	fname = request.form['fname']
	lname = request.form['lname']
	return jsonify({'First Name': fname,'Last Name' : lname})
=======
>>>>>>> 1e26c4e34ec4560a26375b0bb549426d337bb1ea
	

if __name__ == '__main__':
	app.config['DEBUG'] = True #helps you to see changes without re-running app
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 0))
	port = sock.getsockname()[1]
	sock.close()
	app.run(port=port)
