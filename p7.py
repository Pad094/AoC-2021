# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:35:04 2021

@author: pcondon
"""

import numpy as np


def CalculateResultant(inputFile, coordinate):
    resultant = 0
    for value in inputFile:
        resultant+= abs(value - coordinate)
    
    return resultant    


def CalculateResultantPart2(inputFile, coordinate):
    resultant = 0
    for value in inputFile:
        distance = abs(value - coordinate)
        resultant+= distance*(distance+1)/2  
    return resultant    



inputFile = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p7\p7.txt", 'r')
inputFile = [int(x) for x in inputFile.readline().split(",")]



#testInput = [16,1,2,0,4,2,7,1,2,14]
# print(CalculateResulatant(testInput, np.mean(testInput)))

lowerExtreme   = min(inputFile)
topExtreme     = max(inputFile)

#Part 1
bestResultant = CalculateResultant(inputFile, lowerExtreme)
for i in range(lowerExtreme +1, topExtreme + 1):
    if CalculateResultant(inputFile, i) < bestResultant:
        bestResultant = CalculateResultant(inputFile, i)

print("Solution Part 1:", bestResultant)         
        
#Part 2

bestResultant = CalculateResultantPart2(inputFile, lowerExtreme)
for i in range(lowerExtreme +1, topExtreme + 1):
    if CalculateResultantPart2(inputFile, i) < bestResultant:
        bestResultant = CalculateResultantPart2(inputFile, i)

        
print("Solution Part 2:", bestResultant)      




