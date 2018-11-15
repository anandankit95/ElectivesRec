import numpy as np 
import pandas as pd
import random
from sklearn.utils import shuffle

# Electives: Data Analytics (python,python_lab,math,DS,DS_Lab,IDS,LA,CGPA(>9))
# Advanced DBMS (DBMS,CGPA(>7.5))
# Advanced Algo (DS,DS_lab,DML,algo,algo lab,cgpa(>8.5))
# Computer graphics (python,python_lab,LA,cgpa(>6))
# HPCA (ddc0,ddco_lab,mpca,C,C_lab,cgpa(>6.5))
# WT (WT1,WT1_lab,(>6))


#C(0),C_lab(1),Python(2),Pythonlab(3),Math(4),DS(5),DS_lab(6),DML(7),DBMS(8),DBMS_lab(9)
#Algo(10),Algo_lab(11),IDS(12),MPCA(13),DDCO(14),DDCO_lab(15),TOC(16),LA(17),WT1(18),WT1_lab(19)

def data_gen(num,ind,elec):
	good=[8,9,10]
	general=[4,5,6,7,8,9,10]
	data=[]
	for i in range(num):	
		row=[random.choice(general) for i in range(20)]
		for i in ind:
			row[i]=random.choice(good)	
		row.append(elec)		
		data.append(row)
	return(data)	


data=data_gen(100,[2,3,4,5,6,12,17],"DA") #data analytics
data.extend(data_gen(100,[8],"ADBMS"))	#advanced DBMS
data.extend(data_gen(100,[5,6,7,9,11],"ADA")) #advanced algo
data.extend(data_gen(100,[2,3,17],"CG")) #computer graphics
data.extend(data_gen(100,[0,1,13,14,15],"HPCA")) #hpca
data.extend(data_gen(100,[18,19],"WTS")) #WT


df = shuffle(pd.DataFrame(data))
df.columns=["C","C_LAB","PYTHON","PYTHON_LAB","MATH","DS","DS_LAB","DML","DBMS","DBMS_LAB","DAA","DAA_LAB","IDS","MPCA","DDCO","DDCO_lAB","TOC","LA","WT1","WT1_LAB","Elective"]
df.to_csv("erec_data.csv",sep=',', index=False)