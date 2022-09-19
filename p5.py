# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:55:12 2021

@author: Padraig
"""
import numpy as np

inputFile = []
file = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p5\p5.txt", 'r')
for line in file:
    line = line.replace(' ', ',')
    line = line.split(',')
    del line[2]
    line = [int(x) for x in line]
    inputFile.append(line)  

#Format (x1, y1), (x2, y2);
countMatrix = np.zeros((1000,1000))
for line in inputFile:
    if line[0] == line[2]:
        smaller = min(line[1], line[3])
        greater = max(line[1], line[3])
        for i in range(smaller, greater+1):
            countMatrix[line[0], i] +=1
            
    elif line[1] == line[3]:
        smaller = min(line[0], line[2])
        greater = max(line[0], line[2])
        for i in range(smaller, greater+1):
            countMatrix[ i, line[1]] +=1    
            
overlapCount = 0
for i in range(1000):
    for j in range(1000):
        if countMatrix[i,j]>1:
            overlapCount+=1
print("Solution Part 1:", overlapCount)    


#Part 2       
countMatrix = np.zeros((1000,1000))
for line in inputFile:
    if line[0] == line[2]:
        smaller = min(line[1], line[3])
        greater = max(line[1], line[3])
        for i in range(smaller, greater+1):
            countMatrix[line[0], i] +=1
            
    elif line[1] == line[3]:
        smaller = min(line[0], line[2])
        greater = max(line[0], line[2])
        for i in range(smaller, greater+1):
            countMatrix[ i, line[1]] +=1   
            
    else:
        smallerX = min(line[0], line[2])
        greaterX = max(line[0], line[2])  
        
        smallerY = min(line[1], line[3])
        greaterY = max(line[1], line[3])
        
        
        if smallerX == line[0] and smallerY == line[1]:
            for i in range(greaterX+ - smallerX + 1):
                countMatrix[ smallerX +i, smallerY +i] +=1
        elif  smallerX == line[0] and greaterY == line[1]:
            for i in range(greaterX+ - smallerX + 1):
                countMatrix[ smallerX +i, greaterY -i] +=1
                
        elif greaterX == line[0] and smallerY == line[1]:
            for i in range(greaterY+ - smallerY + 1):
                countMatrix[ greaterX -i, smallerY +i] +=1 
        else:
            for i in range(greaterY+ - smallerY + 1):
                countMatrix[ greaterX -i, greaterY -i] +=1 
            
                
            
overlapCount = 0
for i in range(1000):
    for j in range(1000):
        if countMatrix[i,j]>1:
            overlapCount+=1
print("Solution Part 2:",overlapCount)     
            
