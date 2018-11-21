import pandas as pd
import numpy as np

df=pd.read_csv("/Users/ankit/Desktop/Sem 7/Web Tech 2/WT2 Project/ElectivesRec/erec_data.csv")
y=df.iloc[:,-1].values
#print(y)

d = {'DA':0,'ADBMS':0,'ADA':0,'CG':0,'HPCA':0,'WTS':0}
for elem in y:
	if(elem=="DA"):
		d["DA"]+=1
	elif elem =="ADBMS":
		d["ADBMS"]+=1
	elif elem =="ADA":
		d["ADA"]+=1
	elif elem =="CG":
		d["CG"]+=1
	elif elem =="HPCA":
		d["HPCA"]+=1
	elif elem =="WTS":
		d["WTS"]+=1

print(d)					