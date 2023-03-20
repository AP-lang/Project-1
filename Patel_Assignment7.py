# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:50:55 2022

@author: Abhip
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


#read data into data frame, data
data = pd.read_csv("EastWestAirlinesCLuster.csv")

# Fill missing values with mean column values in the data set
#  In this case, Age had some holes
data.fillna(data.mean(), inplace=True)

data = data.drop(['ID#'], axis=1)



print("***** New Data Set *****")
print(data.head())
print("")


print("*****Cluster Analysis*****")
kmeans = KMeans(n_clusters=7).fit(data)

#save the centroid for each cluster
centroids = kmeans.cluster_centers_

#if you don't do this, your centroid values will be in scientific notation
np.set_printoptions(precision=2,suppress=True)

#Print your centroid for each cluster
print(data.columns.values)
print(centroids)
print()


#add new column to data frame to add the cluster label to each row
data['Cluster'] = kmeans.labels_

print(pd.pivot_table(data,index=["Cluster"],values=['Award?'],aggfunc=[len]))
print()

#copy output to Excel file 
writer = pd.ExcelWriter('AirlinesOutput.xlsx')
data.to_excel(writer,index=False)
writer.save()


#***************************
#* Second cluster analysis *
#***************************

#drop the columns that we don't want!
data = data.drop([ 'Flight_miles_12mo', 'Flight_trans_12', 'Cluster',  ], axis=1)

print("*****Second Cluster Analysis*****")
kmeans = KMeans(n_clusters=7).fit(data)

#save the centroid for each cluster
centroids = kmeans.cluster_centers_


np.set_printoptions(precision=2,suppress=True)

#Print your centroid for each cluster
print(data.columns.values)
print(centroids)
print()

#add new column to data frame to add the cluster label to each row
data['Cluster'] = kmeans.labels_

print(pd.pivot_table(data,index=["Cluster"],values=['Award?'],aggfunc=[len]))
print()

#copy output to Excel file named output.xlsx
writer = pd.ExcelWriter('AirlinesOutput2.xlsx')
data.to_excel(writer,index=False)
writer.save()

