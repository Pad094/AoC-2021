# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:50:20 2021

@author: Padraig
"""
import numpy as np
data = []
file = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p11\p11.txt", 'r')
for line in file.readlines():
    line = [x for x in str(line).strip()]
    data.append(line)
    
#10 x 10
embeddedData = np.ones((12,12))*7.4
for i in range(1, 11):
    embeddedData[i, 1:11] = data[i-1]
    
def CheckIfSynchronised(embeddedData):
    if np.count_nonzero(embeddedData==0) == 100:
        return True
    else:
        return False

    
def ProcessStepIteration(embeddedData): 
    
    #Add 1:
        embeddedData   = (embeddedData + np.ones((12,12)))%10
        unchangedFlag  = False
        numberOfLights = np.count_nonzero(embeddedData==0)
        
        usedNodes   = np.zeros((12,12))
        while not unchangedFlag:
            chainUpdate = np.zeros((12,12))
            for i in range(1,11):
                for j in range(1,11):
                    if int(embeddedData[i,j]) ==0:
                        continue
                    
                    numberOfChainUpdates = 0
                    if embeddedData[i-1,j] == 0 and usedNodes[i-1,j] != 1:
                        numberOfChainUpdates +=1
                    if embeddedData[i-1,j-1] == 0 and usedNodes[i-1,j-1] != 1:
                        numberOfChainUpdates +=1
                    if embeddedData[i-1,j+1] == 0 and usedNodes[i-1,j+1] != 1:
                        numberOfChainUpdates +=1
                    if embeddedData[i,j-1] == 0 and usedNodes[i,j-1] != 1:
                        numberOfChainUpdates +=1
                    if embeddedData[i+1,j-1] == 0 and usedNodes[i+1,j-1] != 1:
                        numberOfChainUpdates +=1
                    if embeddedData[i+1,j+1] == 0 and usedNodes[i+1,j+1] != 1:
                        numberOfChainUpdates +=1
                    if embeddedData[i+1,j] == 0 and usedNodes[i+1,j] != 1:
                        numberOfChainUpdates +=1
                    if embeddedData[i,j+1] == 0 and usedNodes[i,j+1] != 1:
                        numberOfChainUpdates +=1  
                    chainUpdate[i,j] = numberOfChainUpdates    
            
             #Mark the used nodes:
            for i in range(1,11):
                for j in range(1,11):
                    if embeddedData[i,j] == 0:
                        usedNodes[i,j]  = 1        
            
            embeddedData = (embeddedData + chainUpdate)
            #Need to replace 11 etc. by 10 again
            for i in range(1,11):
                for j in range(1,11):
                    if embeddedData[i,j] >10  and embeddedData[i,j]%1 < .2:
                        embeddedData[i,j]  = 10
                        
            embeddedData = embeddedData%10  
            if numberOfLights == np.count_nonzero(embeddedData==0):
                unchangedFlag = True
            numberOfLights = np.count_nonzero(embeddedData==0)
            
        return embeddedData, numberOfLights
                    
totalFlashes = 0 
iteration = 0      
while True:
    iteration+=1
    embeddedData, number = ProcessStepIteration(embeddedData) 
    if CheckIfSynchronised(embeddedData):
       # print(iteration)
        break
    totalFlashes+= number

print("Part 2: ", iteration)


def SolvePart1(stringPath):
    
    data = []
    file = open(stringPath, 'r')
    for line in file.readlines():
        line = [x for x in str(line).strip()]
        data.append(line)
        
    #10 x 10

    embeddedData = np.ones((12,12))*7.4
    for i in range(1, 11):
        embeddedData[i, 1:11] = data[i-1]
    totalFlashes = 0
    iteration = 0     
    for i in range(100):
        embeddedData, number = ProcessStepIteration(embeddedData)  
        totalFlashes+= number
        
        
    print("Part 1: ", totalFlashes)   
    
SolvePart1(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p11\p11.txt")    
    