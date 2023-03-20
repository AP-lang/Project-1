# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 13:38:07 2022

@author: Abhip
"""

import pandas as pd

df = pd.read_csv("borderCrossing.csv")

#imports Pandas and reads BoarderCrossing.csv file so I can edit it  in the program

df["Border"].replace("US-Canada Border","Canadian Border",inplace=True)
df["Border"].replace("US-Mexico Border","Mexican Border",inplace=True)

df["Measure"].replace("Rail Containers Empty","Rail Container",inplace=True)
df["Measure"].replace("Rail Containers Full","Rail Container",inplace=True)

df["Measure"].replace("Truck Containers Empty","Train Container",inplace=True)
df["Measure"].replace("Truck Containers Full","Train Container",inplace=True)

##from lines 14 to 21, data from the csv file is changed and replaced.

df = df[["Border", "Port Name","State", "Date","Measure", "Value" ]]

# Line 25 shows specific columns that need to appear in the file.



writer = pd.ExcelWriter('BorderCrossingCleaned.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()

# The information is written into the xlsx file, and gets saved 