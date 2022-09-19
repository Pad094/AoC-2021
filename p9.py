# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:55:13 2021

@author: pcondon
"""
import numpy as np
auxilliaryGrid = np.zeros((102, 102))


def CheckIfMinima(grid, i, j):
    if grid[i,j] < min(grid[i,j+1], grid[i+1, j], grid[i-1, j], grid[i, j-1]):
        return True
    else:
        return False
    
    
def CalculatePart1Score(grid, i, j):
      return 1+ grid[i,j]


def CaclulateBasinSize(grid, i, j):
    auxilliaryGrid[i,j] = 1
    
    if grid[i+1, j] > grid[i, j] and grid[i+1,j] < 9:
        CaclulateBasinSize(grid, i+1, j)
        
    if  grid[i, j+1] > grid[i, j] and grid[i,j+1] < 9:
        CaclulateBasinSize(grid, i, j+1)
    
    if  grid[i-1, j] > grid[i, j] and grid[i-1,j] < 9:
        CaclulateBasinSize(grid, i-1, j)

    if  grid[i, j-1] > grid[i, j] and grid[i,j-1] < 9:
        CaclulateBasinSize(grid, i, j-1)
    





#Grid is 100 x 100
embeddedGrid = np.ones((102, 102))*1000
inputFile = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p9\p9.txt", 'r')
inputFile = inputFile.readlines()



for i in range(len(inputFile)):
    test = str(inputFile[i]).split()
    inputFile[i] = [int(a) for a in test[0]]
    embeddedGrid[i+1, 1:101] = np.array(inputFile[i])
    
  
# #Part 1
totalRiskLevel  =0
for i in range(1,101):
    for j in range(1,101):
        if CheckIfMinima(embeddedGrid, i, j):
            totalRiskLevel += CalculatePart1Score(embeddedGrid, i, j)
print("Solution Part 1:", totalRiskLevel)          

#Part 2
basinSizes = []
auxilliaryGrid = np.zeros((102, 102))
scores = np.zeros((102, 102))
for i in range(1, 101):
    for j in range(1, 101):
      if embeddedGrid[i,j] < 9:
        CaclulateBasinSize(embeddedGrid, i, j)
        scores[i,j] = sum(np.sum(auxilliaryGrid, axis=1))
        auxilliaryGrid = np.zeros((102, 102))
    

for i in range(1,101):
    for j in range(1,101):
        if CheckIfMinima(embeddedGrid, i, j):
            basinSizes.append(scores[i,j])
            
basinSizes = np.sort(basinSizes)
print("Solution Part 2:", basinSizes[-1]*basinSizes[-2]*basinSizes[-3])            
