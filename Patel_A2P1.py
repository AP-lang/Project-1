# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

StuAvg = (95+55+77+88+73)
StuAvg = StuAvg / 5
#First the code calculates the Student Average

# and then the code takes the average and puts it through else-if-statements
if StuAvg >= 90:
    print("Letter: A")
    print("Numeric:" + str(StuAvg))
    
elif StuAvg >= 80:
    print("Letter: B")
    print("Numeric:" + str(StuAvg))
    
elif StuAvg >= 70:
    print("Letter: C")
    print("Numeric:" + str(StuAvg))
    
elif StuAvg >= 60:
        print("Letter: D")
        print("Numeric:" + str(StuAvg))
else:
   print("Letter: F")
   print("Numeric:" + str(StuAvg))
   
# if the student's average falls into any of these ranges, the program prints out
# the letter grade and the Numeric score.
