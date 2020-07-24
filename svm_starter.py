import pandas as pd
import matplotlib.pyplot as plt  
from sklearn import svm
from sklearn import metrics
import joblib
import numpy as np
from sklearn.utils import shuffle

##Step 1: Get Data from CSV
df = pd.read_csv('csv/dataset.csv')
df = df.sample(frac=1).reset_index(drop = True)
print (df)

##Step 2: Seperate Labels and Features
X = df.drop(['label'],axis=1)
Y = df["label"]
#
X_train,Y_Train = X[:200], Y[:200]
X_test , Y_test = X[200:] ,Y[200:] 

#Step 3: Build a Model and Save it
model = svm.SVC(kernel="rbf" , C= 10)
model.fit(X_train,Y_Train) 
joblib.dump(model,"model/svm_9label_linearg7")
##Step4 : Print Accuracy 
prediction = model.predict(X_test)
print ("model score is " ,metrics.accuracy_score(Y_test,prediction))