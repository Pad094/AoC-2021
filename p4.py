# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:34:56 2021

@author: Padraig
"""
import numpy as np


def checkBingo(mat):
    bingo = False
    for i in range(5):
        if -1 not in mat[i, :] or -1 not in mat[:, i]:
            bingo = True
    
    return bingo;        

def ProcessInput(value, mat1, mat2):
    for i in range(100):
         for j in range(5):
            for k in range(5):
                if mat1[i,j,k] == value:
                   mat1[i,j,k] = 0
                   mat2[i,j,k] = value
    return mat1, mat2;               
       
file = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p4\p4.txt", 'r');
callOut = file.readline().split(",");
callOut = [string for string in callOut if string != ""];
callOut = [int(x) for x in callOut];


matrixCount = 0
matrices = []

for line in file:
        if line == "\n":
            count = 0
            nextMat = []
        elif count >=0 & count < 5:
            nextRow = line.split(" ")
            nextRow = [string for string in nextRow if string != ""]
            nextMat.append([int(x) for x in nextRow])
            count +=1
            if count == 5:
                matrices.append(nextMat.copy())
            
matrices = np.array(matrices)


emptyMatrix = np.ones((100,5,5))
emptyMatrix*=-1

stopFlag = False
while True:
    for value in callOut:
        matrices, emptyMatrix = ProcessInput(value, matrices, emptyMatrix)
        for i in range(100):
            if checkBingo(emptyMatrix[i, :, :]):
                stopFlag = True
                break
        if stopFlag:
            break
        
    break
 
   
print("Solution Part 1:", sum(np.sum(matrices[i, :, :], axis = 1))* value)        
   

#Part 2:

for line in file:
        if line == "\n":
            count = 0
            nextMat = []
        elif count >=0 & count < 5:
            nextRow = line.split(" ")
            nextRow = [string for string in nextRow if string != ""]
            nextMat.append([int(x) for x in nextRow])
            count +=1
            if count == 5:
                matrices.append(nextMat.copy())
            
matrices = np.array(matrices)
emptyMatrix = np.ones((100,5,5))
emptyMatrix*=-1

finishedIndices = []
stopFlag = False
while True:
    for value in callOut:
        matrices, emptyMatrix = ProcessInput(value, matrices, emptyMatrix)
        for i in range(100):
           if i not in finishedIndices: 
                if checkBingo(emptyMatrix[i, :, :]):
                    finishedIndices.append(i)
                    if len(finishedIndices) ==100:
                        stopFlag = True
                if stopFlag:        
                  break
                
        if stopFlag:
            break
        
    break
   
print("Solution Part 2:", sum(np.sum(matrices[i, :, :], axis = 1))* value)        
  
            
            
         
            
            
            
            
        
            