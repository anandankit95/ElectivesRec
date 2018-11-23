from flask import Flask,render_template,request,session,redirect, url_for,jsonify
import pymongo
from pymongo import MongoClient
import os
import socket
from flask import jsonify
import json
import numpy as np 
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

# Read username & password from cred file to get acces to database (Replace with your file)


#filename='/Users/ankit/Desktop/Sem 7/Web Tech 2/WT2 Project/ElectivesRec/cred.txt'
#temp=open(filename,'r').read().split('\n')

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
@app.route('/',methods=['GET','POST'])
def register():
	error = None
	if request.method == 'POST':
		print("Hello")
		auc=db["credentials"]
		u_name=request.form['uname']
		email=request.form['email']
		usn=request.form['USN']
		pwd=request.form['password']
		flag1=auc.find_one({"uname":u_name})
		flag2=auc.find_one({"usn":usn})
		if(not(flag1) and not(flag2)):
			post={"uname":u_name,"email":email,"usn":usn,"passwd":pwd}
			print(post)
			auc.insert_one(post)
			return render_template('login.html')
		else:
			error = "Existing user"	
	return render_template('register.html')
	
# User login page 	
@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		auc=db["credentials"]
		user=auc.find_one({"uname":request.form['username']})
		if(user!=None) :
			if(request.form['password']==user["passwd"]):
				return(redirect(url_for('elective')))
			else:
				error = "Invalid password"
		else:
			error = "Invalid username"					
	return(render_template('login.html',error=error))



def predict(X,Y,vals):
	le = preprocessing.LabelEncoder()
	le.fit(["DA","ADBMS","ADA","CG","HPCA","WTS"])
	Y=le.transform(Y) 
	clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X,Y)
	Y_pred=clf.predict_proba([vals])[0]
	d={}
	ls=le.inverse_transform(range(6))
	for i in range(6):
		d[ls[i]]=Y_pred[i]	
	return(d)



# Elective form input page
@app.route('/elective',methods=['GET','POST'])
def elective():
	#if(request.method == 'GET'):
		#return render_template('elecFormProgressive.html')

	if(request.method == 'POST'):
		result = request.form
		#print(result)
		arr=sorted([i for i in result]) 
		arr.remove('fname')
		arr.remove('lname')
		vals=[int(result[i]) for i in arr]
		acad=db["academics"]
		data=pd.DataFrame(list(acad.find()))
		Y=data[['Elective']].values
		df=data.drop('Elective',1)
		df=df.drop('_id',1)
		X=df.values
		predictions=predict(X,Y,vals)
		print(predictions)
		return jsonify({"DA":predictions["DA"],"ADBMS":predictions["ADBMS"],"WTS":predictions["WTS"],"HPCA":predictions["HPCA"],"ADA":predictions["ADA"],"CG":predictions["CG"]})
		
	   	
	return render_template('elecFormProgressive.html',)





if __name__ == '__main__':
	app.config['DEBUG'] = True #helps you to see changes without re-running app
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 0))
	port = sock.getsockname()[1]
	sock.close()
	app.run(port=port)
