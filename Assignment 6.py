# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:19:35 2022

@author: Abhip
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
#from sklearn.preprocessing import LabelEncoder


np.set_printoptions(precision=3, suppress=True)


data = pd.read_csv("winequality.csv")

data.fillna(data.mean(), inplace=True)






x = StandardScaler().fit_transform(data)

scaler = StandardScaler()

scaler.fit(data)
normalData = scaler.transform(data)


pca = PCA()
transformedPCA = pca.fit_transform(normalData)





print("Explained variance:", pca.explained_variance_)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Cumulative explained variance ratio:", pca.explained_variance_ratio_.cumsum())
print()


print("Feature Weights")

for i in data.columns: 
    print(i, end=' ') 

print()
print(abs( pca.components_ ))


weights = pd.DataFrame(abs(pca.components_))
weights.columns = data.columns


writer = pd.ExcelWriter('output.xlsx')
weights.to_excel(writer,index=False)
writer.save()



print()
print('###############################################')
print()

data = data.drop(['residual sugar', 'density', 'pH', 'alcohol', 'fixed acidity','volatile acidity', 'chlorides'], axis=1)

scaler = StandardScaler()
scaler.fit(data)
normalData = scaler.transform(data)

pca = PCA()
transformedPCA = pca.fit_transform(normalData)

print("Explained variance:", pca.explained_variance_)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Cumulative explained variance ratio:", pca.explained_variance_ratio_.cumsum())
print()


print("Feature Weights")

for i in data.columns: 
    print(i, end=' ') 

print()
print(abs( pca.components_ ))


weights2 = pd.DataFrame(abs(pca.components_))
weights2.columns = data.columns


writer2 = pd.ExcelWriter('output2.xlsx')
weights2.to_excel(writer2,index=False)
writer2.save()




