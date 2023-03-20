# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:18:03 2022

@author: Abhip
"""

import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix


#read data into data frame, data
data = pd.read_csv("winequality.csv")

# Fill missing values with mean column values in the data set
#  In this case, Age had some holes
data.fillna(data.mean(), inplace=True)

#drop the columns that we don't need!
data = data.drop([ 'free sulfur dioxide', 'sulphates'], axis=1)

#list all of the predictors that will be used
predictors = ['residual sugar', 'pH', 'alcohol', 'volatile acidity', 'chlorides']
#set up target, predictors, and split the training/testing partitions
X = data[predictors]
y = data['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#Normalize your data Here!!
scaler = StandardScaler()

# Fit only to the training data
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#####################################################################

print("Model 1 - (7) with relu activation function")
#create the neural network with your choice of hidden layer size
#If your sample size is NOT in the thousands, use solver='lbfgs'
network = MLPClassifier(hidden_layer_sizes=(20), max_iter=2000, solver='lbfgs')
network.fit(X_train, y_train)

#test the model against our new model and calculate the accuracy
pred = network.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred),3))

#create confusion matrix and print it
confusionMatrix = pd.DataFrame(
    confusion_matrix(y_test, pred),
    columns=['Predicted Low Value', 'Predicted High Value'],
    index=['True Low Value', 'True High Value']
)
print(confusionMatrix)
print()








confusionMatrix = pd.DataFrame(
    confusion_matrix(y_test, pred),
    columns=['Predicted Not delayed', 'Predicted delayed'],
    index=['True Not delayed', 'True delayed']
)
print(confusionMatrix)
print()













#####################################################################

print("Model 2 - (10,10) with logistic activation function")
#create the neural network with your choice of hidden layer size
#If your sample size is NOT in the thousands, use solver='lbfgs'
network2 = MLPClassifier(hidden_layer_sizes=(10,10),max_iter=400,solver='lbfgs',activation='relu')
network2.fit(X_train, y_train)

#test the model against our new model and calculate the accuracy
pred = network2.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred),3))

#create confusion matrix and print it
confusionMatrix = pd.DataFrame(
    confusion_matrix(y_test, pred),
    columns=['Predicted bad', 'Predicted good'],
    index=['True bad', 'True good']
)
print(confusionMatrix)
print()