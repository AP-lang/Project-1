# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 23:17:48 2022

@author: Abhip
"""
with open('trash.txt', mode='w') as myFile:
  myFile.writelines('40 50 98 43 20\n')
  myFile.writelines('10 67 84 25 71\n')
  myFile.writelines('37 54 32 90 62\n')
  myFile.writelines('76 49 69 95 44\n')
  myFile.writelines('11 22 33 44 55\n')
    

  
import numpy as np 

numbers = np.array([40, 50, 98, 43, 20])
numbersTwo = np.array([[10, 67, 84, 25, 71],
                       [37, 54, 32, 90, 62],
                        [76, 49, 69, 95, 44],
                        [11, 22, 33, 44, 55,]])

#Created an array called numbers and numbersTwo 

load = np.loadtxt('trash.txt', int)

CntA,CntB,CntC,CntD = 0,0,0,0

QuA,QuB,QuC,QuD = 0,0,0,0

# Line 26 helps get the standard deviation
# Lines 28 and 30 sets the counters to zeros, to obtain the quartiles and count of ABCD


ArraySum = np.sum(numbers) + np.sum(numbersTwo)
print ("Sum:",ArraySum)
## ArraySum calculates the sum of numbers and numberstwo

ArrayTotal = np.size(numbers) + np.size(numbersTwo)

ArrayAvg = ArraySum / ArrayTotal

print('Average:',ArrayAvg)

# Array total is needed to find the total amount of numbers in the array
# Once the array total amount is found, you can calulate the Average by dividing the ArraySum by the ArrayTotal

ArrayStd = np.std(load)
print('Std:' ,ArrayStd)

# ArrayStd finds the standard deviation of the array.




with open('myOutput.txt', 'w+') as MyOut:
    for numbers in load:
        for load in numbers:
            if load >= 1 and load <= 25:
                      
                      CntA = CntA + 1
                      QuA +=1
                      
            elif load >= 26 and load <= 50:
                    
                    CntB = CntB + 1
                    QuB +=1
            elif load >= 51 and load <= 75:
                    
                    CntC = CntC + 1
                    QuC +=1
            elif load >= 76 and load <= 100:
                 
                    CntD = CntD + 1
                    QuD +=1
# Gives the counter for how many times numbers fall into each quartile.
MyOut = open('myOutput.txt', 'w+')

for count in numbers + numbersTwo:
        for value in count:
            if value >=1 and value <=25:
                QuA +=1
               
                MyOut.write(f'{value} A\n')
                
            elif value >=26 and value <=50:
                QuB +=1
                
               
                MyOut.write(f'{value} B\n')
            elif value >=51 and value <= 75:
                QuC +=1
                
                MyOut.write(f'{value} C\n')
            else:
                QuD +=1
                
                MyOut.write(f'{value} D\n')
# This is the counter shows which quartile they belong to. 
         
MyOut = open('myOutput.txt', 'w+')




MyOut.write(f'A {CntA}\n')
MyOut.write(f'B {CntB}\n')
MyOut.write(f'C {CntC}\n')
MyOut.write(f'D {CntD}\n')
MyOut.write("   \n")

## The count of numbers that fall into the quartile

MyOut.close()
