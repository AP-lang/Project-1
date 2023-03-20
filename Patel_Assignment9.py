# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:39:45 2022

@author: Abhip
"""
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt




data = pd.read_csv("FlightDelays.csv")

data.fillna(data.mean(), inplace=True)


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






predictors = ['DEST', 'FL_NUM', 'Weather',  'TIME_SLOT' ]

X = data[predictors]
y = data['Flight Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

estimator = DecisionTreeClassifier()
estimator.fit(X_train, y_train)


print('depth','gini ','entropy')
for i in range(1,7):
    dtree = DecisionTreeClassifier(criterion='gini', max_depth=i)
    dtree.fit(X_train, y_train)
    pred = dtree.predict(X_test)
    gini_score = accuracy_score(y_test, pred)
    ####
    dtree = DecisionTreeClassifier(criterion='entropy', max_depth=i)
    dtree.fit(X_train, y_train)
    pred = dtree.predict(X_test)
    entropy_score = accuracy_score(y_test, pred)

    #print(i,round(gini_score,3),round(entropy_score,3))
    print(f'{i:<6}{round(gini_score,3):<6}{round(entropy_score,3)}')
    ####

print()
print()



dtree = DecisionTreeClassifier(criterion='entropy', max_depth=3)
dtree.fit(X_train, y_train)


pred = dtree.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred),3))

confusionMatrix = pd.DataFrame(
    confusion_matrix(y_test, pred),
    columns=['Predicted Not delayed', 'Predicted delayed'],
    index=['True Not delayed', 'True delayed']
)
print(confusionMatrix)
print()

importances = pd.DataFrame({'predictor':X_train.columns,'importance':np.round(dtree.feature_importances_,3)})
importances = importances.sort_values('importance',ascending=False)
print(importances)
print()

plt.figure()
plot_tree(dtree, filled=True, feature_names=predictors, class_names=['FlightDelayed','ontime'])
plt.savefig('treePlot.pdf')
plt.show()



























