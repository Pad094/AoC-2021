# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 23:07:46 2021

@author: Padraig
"""

#p12
vtxs = set({})
edges = []
file = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p12\p12.txt", 'r')
line = file.readline()
while line.strip():
    line = line.split("-")
    line = [x.strip() for x in line]
    vtxs.add(line[0])
    vtxs.add(line[1])
    edges.append(line)
    line = file.readline()
    
edgeDictionary ={}
for vtx in vtxs:
    edgeDictionary[vtx] =set()
for edge in edges:
    edgeDictionary[edge[0]].add(edge[1])
    edgeDictionary[edge[1]].add(edge[0])


def CheckIfEndCannotBeReached(vtxs, edgeDictionary, ForbiddenSet, startVtx):
    PossibleMoves = edgeDictionary[startVtx] - ForbiddenSet
    if len(PossibleMoves) < 1:
        return False
    
    for i in range(40):
        for move in PossibleMoves:
            PossibleMoves = PossibleMoves.union(edgeDictionary[move] - ForbiddenSet)
            if any(x.islower() for x in PossibleMoves):
                return True
            
    return False       
    
    


def CountPathsFromVertexPart1(vtxs, edgeDictionary, ForbiddenSet, startVtx, path):
    path.append(startVtx)
        
    
    if startVtx == "end":
        return 1

    PossibleMoves = edgeDictionary[startVtx] - ForbiddenSet
    
    if not CheckIfEndCannotBeReached(vtxs, edgeDictionary, ForbiddenSet, startVtx):
        return 0
    
    if PossibleMoves == set():
        return 0
    
    answer = 0
    for move in PossibleMoves:
        if move[0].islower():
            newForbidden  = ForbiddenSet.copy()
            newForbidden.add(move)
            answer += CountPathsFromVertexPart1(vtxs, edgeDictionary, newForbidden, move, path)
               
        else:
            answer += CountPathsFromVertexPart1(vtxs, edgeDictionary, ForbiddenSet, move, path)
    return answer
 
    
 
def CountPathsFromVertexPart2(vtxs, edgeDictionary, ForbiddenSet, startVtx, latestPath, specialPowerUsed, pathsSave): 

    path = latestPath.copy()
    path.append(startVtx)
    
        
    if startVtx == "end":
        if path in pathsSave:
            return 0
        pathsSave.append(path)
        if len(pathsSave)%10000 ==1:
            print(len(pathsSave))
        return 1
       
    
    
    PossibleMoves = edgeDictionary[startVtx] - ForbiddenSet
    
    if not CheckIfEndCannotBeReached(vtxs, edgeDictionary, ForbiddenSet, startVtx):
        return 0
    
    if PossibleMoves == set():
        return 0
    
    answer = 0
    for move in PossibleMoves:
        
        if move[0].islower():
            if specialPowerUsed == 0 and move != "end":
                newForbidden  = ForbiddenSet.copy()
                newForbidden.add(move)
                path1 = path.copy()
                path2 = path.copy()
                answer +=  CountPathsFromVertexPart2(vtxs, edgeDictionary, newForbidden, move, path1, 0, pathsSave)  \
                    + CountPathsFromVertexPart2(vtxs, edgeDictionary, ForbiddenSet, move, path2, 1, pathsSave)
            else:
                newForbidden  = ForbiddenSet.copy()
                newForbidden.add(move)
                answer += CountPathsFromVertexPart2(vtxs, edgeDictionary, newForbidden, move, path, 1, pathsSave)
              
        else:
            answer += CountPathsFromVertexPart2(vtxs, edgeDictionary, ForbiddenSet, move, path, specialPowerUsed, pathsSave)
        
    return answer  


print("Solution Part 1:", CountPathsFromVertexPart1(vtxs, edgeDictionary, {'start'}, 'start', [])) 
print("Solution Part 2:", CountPathsFromVertexPart2(vtxs, edgeDictionary, {'start'}, 'start', [], 0, []))  