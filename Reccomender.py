import numpy as np 
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

df=pd.read_csv("/Users/ankit/Desktop/Sem 7/Web Tech 2/WT2 Project/ElectivesRec/erec_data.csv")
X=df.iloc[:,:-1].values
le = preprocessing.LabelEncoder()
Y=df.iloc[:,[-1][0]].values
le.fit(["DA","ADBMS","ADA","CG","HPCA","WTS"])
Y=le.transform(Y) 
clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X,Y)
#print(cross_val_score(clf,X,Y,cv=10))
Y_pred=clf.predict_proba([[9,10,8,9,10,9,9,8,8,7,10,8,9,8,8,9,8,8,9,10]])
print(Y_pred)
return Y_pred
#print(le.inverse_transform(Y_pred))
#print(accuracy_score(Y,Y_pred))