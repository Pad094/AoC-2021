# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 08:39:15 2022

@author: Padraig
"""
import sys
import fileinput
import copy 

#File Input
sys.argv[0] = r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p25\p25.txt"

class Grid():
    
    def __init__(self, file):
        self._grid         = [split(line.strip()) for line in file]
        self._previousGrid = []
        
    def PrintGrid(self):
        for line in self._grid:
            print(line)
            
    def ProcessIteration(self):
        self._previousGrid = copy.deepcopy(self._grid)
        #Process Eastward Direction First:
        for i in range(len(self._previousGrid)):
            #line = self._previousGrid[i]
            if self._previousGrid[i][-1] == ">" and self._previousGrid[i][0] == ".":
                self._grid[i][0]  = ">"
                self._grid[i][-1] = "."
            for j in range(len(self._previousGrid[i])-1):
                if self._previousGrid[i][j] == ">" and self._previousGrid[i][j+1] ==".":
                    self._grid[i][j]   = "."
                    self._grid[i][j+1] = ">"
                    
       #Then Process Northward Direction:
           #Loop Columns this time
        newGrid = copy.deepcopy(self._grid)
        for i in range(len(self._previousGrid[0])):      
            if self._grid[-1][i] == "v" and self._grid[0][i] == ".":
                newGrid[0][i] = "v"
                newGrid[-1][i] = "."
            for j in range(len(self._previousGrid)-1):
                if self._grid[j][i] == "v" and self._grid[j+1][i] ==".":
                    newGrid[j][i]   = "."
                    newGrid[j+1][i] = "v"
        
        self._grid = copy.deepcopy(newGrid)  
        
    def IsGridFixed(self):
        for i in range(len(self._grid)):
            if self._grid[i] != self._previousGrid[i]:
                return False
        return True    
             
                    
    def IterateUntilFixed(self):
        self.ProcessIteration() 
        count = 1
        while not self.IsGridFixed():
            self.ProcessIteration() 
            count += 1
            
        print("Answer Part 1:", count)
        
            
            
           

    

def split(word):
    return [char for char in word] 


if __name__ == "__main__":
    grid = Grid(fileinput.input(sys.argv[0]))
    #grid.PrintGrid()
    grid.IterateUntilFixed()
    #print("Iteration Processed")
    #grid.PrintGrid()
    #print(grid.IsGridFixed())
    
    
    
   