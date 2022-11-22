# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:48:13 2022

@author: Padraig
"""
import numpy as np


with open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p20\p20.txt") as file:
    
    counter = 0
    grid    = []
    for line in file:
        if counter ==0:
            imageMap = list(line.strip())
            counter +=1
            continue
            
        elif counter ==1:
            counter +=1
            continue
        
        grid.append(list(line.strip()))
    grid = np.array(grid) 
    
    
def EmbedGrid(grid, var):
    blankLine = [var for x in range(grid.shape[1] + 2)]
    newGrid = [blankLine]
    for i in range(grid.shape[0]):
        nextLine = [var]
        for x in grid[i, :]:
            nextLine.append(x)
        nextLine.append(var)    
        newGrid.append(nextLine)
        
    newGrid.append(blankLine)    
    return np.array(newGrid)

def EvaluateValueIJ(grid, imageMap, i, j):
    mapping = {".":"0", "#":"1"}
    evaluationString = mapping[grid[i-1,j-1]] + mapping[grid[i-1, j]] + mapping[grid[i-1, j+1]]+ mapping[grid[i,j-1]] + mapping[grid[i, j]] + mapping[grid[i, j+1]] \
                       + mapping[grid[i+1,j-1]] + mapping[grid[i+1, j]] + mapping[grid[i+1, j+1]]
    
    mapIndex = 0
    for i in range(len(evaluationString)):                
        mapIndex += int(evaluationString[i])*2**(9-i-1)
    return imageMap[mapIndex]            


def CountLightPixels(grid):
    count = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] == "#":
                count +=1
    return count            

def ProcessGridIteration(grid, imageMap, extension):
    
    if extension == ".":
        var  = imageMap[0]
    else:
        var = imageMap[-1]
        
    newGrid1 = EmbedGrid(grid.copy(), extension)
    newGrid1 = EmbedGrid(newGrid1, extension)
    
   
    newGrid2 = EmbedGrid(grid.copy(), extension)
    newGrid2 = EmbedGrid(newGrid2, var)

    
    for i in range(1,newGrid1.shape[0]-1):
        for j in range(1,newGrid1.shape[1]-1):
            newGrid2[i, j] = EvaluateValueIJ(newGrid1, imageMap, i, j)
            
    return newGrid2


def Solution(grid, imageMap, iterations):
    processedGrid = grid.copy()
    extension = "."
    for i in range(iterations):
        print(i)
        processedGrid = ProcessGridIteration(processedGrid.copy(), imageMap, extension)
        if extension == ".":
            extension = imageMap[0]
        else:
            extension = imageMap[-1]   
    return  CountLightPixels(processedGrid)

print("Solution Part 1: ", Solution(grid, imageMap, 2)) 


print("Solution Part 2: ", Solution(grid, imageMap, 50))    
    
            