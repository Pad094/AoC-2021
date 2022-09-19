# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 08:37:42 2021

@author: pcondon
"""

import numpy as np

file = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p13\p13.txt", 'r')
coordinates = []
line = file.readline()
while line.strip():
    line = line.strip()
    coordinate = line.split(",")
    coordinate = [int(x) for x in coordinate]
    coordinates.append(coordinate)
    line= file.readline()
  
    
instructions = []
line = file.readline()
while line.strip():
    line = line.strip()
    instruction = line.replace("=", " ").split(" ")
    instructions.append(instruction[2:4])
    line= file.readline()
    

maxValueX = max([x[1] for x in coordinates])
maxValueY = max([x[0] for x in coordinates])
print(maxValueX,maxValueY)


Grid = np.zeros((maxValueX+1, maxValueY+1))
for coordinate in coordinates:
    Grid[coordinate[1], coordinate[0]] = 1
    
    
print(Grid)


# def AddGrids(Grid1, Grid2):
#     newGrid = np.zeros(max(Grid1.shape[0], Grid2.shape[0]), max(Grid1.shape[1], Grid2.shape[1]));
    
#     for i in range(newGrid.shape[0]):
#         for j in range(newGrid.shape[1]):
#             if 

def FoldGrid(Grid, orientation, lineValue):
    
    if orientation == "x":

            Grid2 = Grid[:, lineValue+1:].copy()
            Grid1 = Grid[:, 0:lineValue].copy()
            
            #Reverse Grid1:
            for i in range(Grid.shape[0]):
                reversedLine = Grid2[i, :]
                reversedLine = reversedLine[::-1]
                Grid2[i, :]  = reversedLine
            
            #Buff Smaller Grid
            if Grid1.shape[1] > Grid2.shape[1]:
                for i in range(Grid1.shape[1] - Grid2.shape[1]):
                    nextRow = np.zeros(Grid1.shape[0])
                    nextRow.shape = (Grid1.shape[0],1)
                    Grid2 = np.c_[nextRow, Grid2] 
                                  
                                  
            if Grid1.shape[1] < Grid2.shape[1]:
                for i in range(Grid1.shape[1] - Grid2.shape[1]):
                    nextRow = np.zeros(Grid1.shape[0])
                    nextRow.shape = (Grid1.shape[0],1)
                    Grid1 = np.c_[nextRow, Grid1] 
                

            Grid3 = np.add(Grid1,Grid2)
            for i in range(Grid3.shape[0]):
                 for j in range(Grid3.shape[1]):
                     if Grid3[i,j] >1:
                         Grid3[i,j] = 1
                         
            return Grid3 
     
        
     
    if orientation == "y":

            Grid2 = Grid[lineValue+1:, :].copy()
            Grid1 = Grid[0:lineValue, :].copy()
            
            #Reverse Grid1:
            for i in range(Grid.shape[1]):
                reversedLine = Grid2[:, i]
                reversedLine = reversedLine[::-1]
                Grid2[:, i]  = reversedLine
            
            #Buff Smaller Grid
            if Grid1.shape[0] > Grid2.shape[0]:
                for i in range(Grid1.shape[0] - Grid2.shape[0]):
                    nextRow = np.zeros(Grid1.shape[1])
                    nextRow.shape = (1, Grid1.shape[1])
                    Grid2 = np.r_[nextRow, Grid2]
                                  
                                  
            if Grid1.shape[0] < Grid2.shape[0]:
                for i in range(Grid1.shape[0] - Grid2.shape[0]):
                    nextRow = np.zeros(Grid1.shape[1])
                    nextRow.shape = (1, Grid1.shape[1])
                    Grid1 = np.r_[nextRow, Grid1]  
                

            Grid3 = np.add(Grid1,Grid2)
            for i in range(Grid3.shape[0]):
                 for j in range(Grid3.shape[1]):
                     if Grid3[i,j] >1:
                         Grid3[i,j] = 1
                         
            return Grid3
        
#Part 1       
print(np.count_nonzero(FoldGrid(Grid, instructions[0][0], int(instructions[0][1]))  ==1))
# print(instructions[0])
#print(FoldGrid(Grid, instructions[0][0], int(instructions[0][1])))



#print(instructions)
for line in instructions:
    #print(line)
    Grid = FoldGrid(Grid, line[0], int(line[1]))
    
#Use variable explorer in spyder to visualise grid    
   
 