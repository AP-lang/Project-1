# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 13:14:56 2022

@author: Abhip
"""

import random
FDie = random.randrange(1,7)
SDie = random.randrange(1,7)

#FDie and SDie stands for First Die, and Second Die
#FDie and SDie get randomized by a set range; 1 to 6

print ("Die #1:", FDie )
print ("Die #2:", SDie)

# The randomized results for each die is then printed out

DieSum = FDie + SDie

print ("Total:", DieSum)

#DieSum is the sum of FDie and SDie
#DieSum is then printed out. 
