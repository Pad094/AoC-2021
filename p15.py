# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 08:55:06 2021

@author: pcondon
"""

import numpy as np
file = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p15\p15.txt", 'r')
file = file.readlines()

adjacencyMartixWeights = []
for line in file:
    line = [int(x) for x in line.strip()]
    adjacencyMartixWeights.append(line)
    

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
infi = 1000000000
   
# Class of the node
class Node:
   
    # Adjacency list that shows the
    # vertexNumber of child vertex
    # and the weight of the edge   
    def __init__(self, vertexNumber):       
        self.vertexNumber = vertexNumber
        self.children = []
   
    # Function to add the child for
    # the given node
    def Add_child(self, vNumber, length):   
        p = Pair(vNumber, length)
        self.children.append(p)
       
# Function to find the distance of
# the node from the given source
# vertex to the destination vertex
def dijkstraDist(g, s, path):
       
    # Stores distance of each
    # vertex from source vertex
    dist = [infi for i in range(len(g))]
   
    # bool array that shows
    # whether the vertex 'i'
    # is visited or not
    visited = [False for i in range(len(g))]
     
    for i in range(len(g)):       
        path[i] = -1
    dist[s] = 0
    path[s] = -1
    current = s
   
    # Set of vertices that has
    # a parent (one or more)
    # marked as visited
    sett = set()    
    while (True):
           
        # Mark current as visited
        visited[current] = True
        for i in range(len(g[current].children)): 
            v = g[current].children[i].first      
            if (visited[v]):
                continue
   
            # Inserting into the
            # visited vertex
            sett.add(v)
            alt = dist[current] + g[current].children[i].second
   
            # Condition to check the distance
            # is correct and update it
            # if it is minimum from the previous
            # computed distance
            if (alt < dist[v]):      
                dist[v] = alt
                path[v] = current;       
        if current in sett:           
            sett.remove(current);       
        if (len(sett) == 0):
            break
   
        # The new current
        minDist = infi
        index = 0
   
        # Loop to update the distance
        # of the vertices of the graph
        for a in sett:       
            if (dist[a] < minDist):          
                minDist = dist[a]
                index = a     
        current = index  
    return dist
   
# Function to print the path
# from the source vertex to
# the destination vertex
def printPath(path, i, s):
    if (i != s):
           
        # Condition to check if
        # there is no path between
        # the vertices
        if (path[i] == -1):       
            print("Path not found!!")
            return       
        #printPath(path, path[i], s)
        #print(path[i] + " ")
      
# Driver Code
if __name__=='__main__':
     
    
    numberOfRows = len(adjacencyMartixWeights)
    numberOfCols = len(adjacencyMartixWeights[0])
    v = []
    n = numberOfRows*numberOfCols
    s = 0
   
    for i in range(n):
        a = Node(i)
        v.append(a)
    
    for i in range(numberOfRows):
       for j in range(numberOfCols):
           if  i < numberOfRows -1 and j < numberOfCols -1:            
                   v[numberOfCols*i + j].Add_child(numberOfCols*(i+1) + j, adjacencyMartixWeights[i+1][j])
                   v[numberOfCols*i + j].Add_child(numberOfCols*(i) + j+1, adjacencyMartixWeights[i][j+1])
                   v[numberOfCols*(i+1) + j].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i][j])
                   v[numberOfCols*i + (j+1)].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i][j])                   
           if i < numberOfRows -1  and j == numberOfCols -1:
                   v[numberOfCols*i + j].Add_child(numberOfCols*(i+1) + j, adjacencyMartixWeights[i+1][j])
                   v[numberOfCols*(i+1) + j].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i][j])
           if i == numberOfRows -1  and j < numberOfCols -1:
                   v[numberOfCols*i + j].Add_child(numberOfCols*(i) + j+1, adjacencyMartixWeights[i][j+1])
                   v[numberOfCols*i + (j+1)].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i][j])
                  

    
    path = [0 for i in range(len(v))]
    dist = dijkstraDist(v, s, path)
    #print(dist)
    

    
def BuildPart2Graph(adjacencyMatrix):
    
    baseGraph = np.array(adjacencyMatrix)
    numberOfRows = len(adjacencyMartixWeights)
    numberOfCols = len(adjacencyMartixWeights[0])
    part2Matrix =   np.zeros((5*numberOfRows, 5*numberOfCols))
    for  i in range(5):
        for j in range(5):         
               nextSlot =  (baseGraph +  np.ones((numberOfRows, numberOfCols))*(i+j))
               for ii in range( numberOfRows):
                   for jj in range( numberOfCols):
                       if nextSlot[ii,jj] > 9:
                           nextSlot[ii,jj] +=1
               part2Matrix[i*numberOfRows: (i+1)*numberOfRows, j*numberOfCols: (j+1)*numberOfCols] = nextSlot%10           
               
    return part2Matrix


#Part 1 
numberOfRows = len(adjacencyMartixWeights)
numberOfCols = len(adjacencyMartixWeights[0])
v = []
n = numberOfRows*numberOfCols
s = 0

for i in range(n):
     a = Node(i)
     v.append(a)
 
for i in range(numberOfRows):
    for j in range(numberOfCols):
        if  i < numberOfRows -1 and j < numberOfCols -1:            
                v[numberOfCols*i + j].Add_child(numberOfCols*(i+1) + j, adjacencyMartixWeights[i+1][j])
                v[numberOfCols*i + j].Add_child(numberOfCols*(i) + j+1, adjacencyMartixWeights[i][j+1])
                v[numberOfCols*(i+1) + j].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i][j])
                v[numberOfCols*i + (j+1)].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i][j])                   
        if i < numberOfRows -1  and j == numberOfCols -1:
                v[numberOfCols*i + j].Add_child(numberOfCols*(i+1) + j, adjacencyMartixWeights[i+1][j])
                v[numberOfCols*(i+1) + j].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i][j])
        if i == numberOfRows -1  and j < numberOfCols -1:
                v[numberOfCols*i + j].Add_child(numberOfCols*(i) + j+1, adjacencyMartixWeights[i][j+1])
                v[numberOfCols*i + (j+1)].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i][j]) 


path = [0 for i in range(len(v))]
dist = dijkstraDist(v, s, path)
print("Solution Part 1:", dist[-1])                

#Part 2
adjacencyMartixWeights =  BuildPart2Graph(adjacencyMartixWeights)
#print(adjacencyMartixWeights)
numberOfRows = len(adjacencyMartixWeights)
numberOfCols = len(adjacencyMartixWeights[0])
v = []
n = numberOfRows*numberOfCols
s = 0

for i in range(n):
     a = Node(i)
     v.append(a)
 
for i in range(numberOfRows):
    for j in range(numberOfCols):
        if  i < numberOfRows -1 and j < numberOfCols -1:            
                v[numberOfCols*i + j].Add_child(numberOfCols*(i+1) + j, adjacencyMartixWeights[i+1,j])
                v[numberOfCols*i + j].Add_child(numberOfCols*(i) + j+1, adjacencyMartixWeights[i,j+1])
                v[numberOfCols*(i+1) + j].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i,j])
                v[numberOfCols*i + (j+1)].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i,j])                   
        if i < numberOfRows -1  and j == numberOfCols -1:
                v[numberOfCols*i + j].Add_child(numberOfCols*(i+1) + j, adjacencyMartixWeights[i+1,j])
                v[numberOfCols*(i+1) + j].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i,j])
        if i == numberOfRows -1  and j < numberOfCols -1:
                v[numberOfCols*i + j].Add_child(numberOfCols*(i) + j+1, adjacencyMartixWeights[i,j+1])
                v[numberOfCols*i + (j+1)].Add_child(numberOfCols*i + j, adjacencyMartixWeights[i,j]) 
               

 
path = [0 for i in range(len(v))]
dist = dijkstraDist(v, s, path)
print("Solution Part 2:", dist[-1])