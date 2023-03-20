# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:16:12 2022

@author: Abhip
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix


data = pd.read_csv("KNN_FlightDelays.csv")

data = data.drop(['DAY_OF_MONTH'], axis=1)


labelEncoder = LabelEncoder()
labelEncoder.fit(data['ORIGIN'])
data['ORIGIN'] = labelEncoder.transform(data['ORIGIN'])



labelEncoder = LabelEncoder()
labelEncoder.fit(data['DEST'])
data['DEST'] = labelEncoder.transform(data['DEST'])


labelEncoder = LabelEncoder()
labelEncoder.fit(data['CARRIER'])
data['CARRIER'] = labelEncoder.transform(data['CARRIER'])


labelEncoder = LabelEncoder()
labelEncoder.fit(data['Flight Status'])
data['Flight Status'] = labelEncoder.transform(data['Flight Status'])

# Fill missing values with mean column values in the data set
#  In this case, Age had some holes
data.fillna(data.mean(), inplace=True)

#List all of the predictors needed - DO NOT include the target
predictors = ['DEST', 'FL_NUM', 'Weather', 'TIME_SLOT']

#set up target, predictors, and split the training/testing partitions
X = data[predictors]
y = data['Flight Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#Normalize your data Here!!
scaler = StandardScaler()

# Fit only to the training data
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#knn = KNeighborsClassifier(n_neighbors=7, metric='euclidean')

#Calculate the optimal k based on test partition accuracy
k_range = range(1,41)
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train,y_train)
    pred=knn.predict(X_test)
    acc=accuracy_score(y_test,pred)
    print(k, round(acc,3))
    
#Create a kNN model with recommended k (7)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train,y_train)

#test model against test partition
pred = knn.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred),3))
print()

confusionMatrix = pd.DataFrame(
    confusion_matrix(y_test, pred),
   columns=['Predicted Ontime', 'Predicted delayed'],
    index=['True Ontime', 'True delayed']
)
print(confusionMatrix)