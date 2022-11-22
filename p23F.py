# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:08:55 2021

@author: Padraig
"""
import heapq
import cProfile

costsDictionary = {0:1, 1:10, 2:100, 3:1000}

podIndices = ["A", "B", "C", "D"]

dictionaryPodIndices ={"A":0, "B":1, "C":2, "D":3}

def FindShortestPath(startConfigHall, startConfigRooms):
  
    

    start = Configuration([None]*11, startConfigRooms)
    visitedIndicator = set()
    heap = [(0, start, ())]
    solutions = []
    #Implement Dijkstra which implementation that only care about vertices we invole into
    #Until we hit end state:
    #Cool evolving Dijkstra version
    #Heap helps with Dijkstra implementation    
    while heap:
        cost, state, path = heapq.heappop(heap)
        if state in visitedIndicator:
            continue

        #print(len(visitedIndicator))
       
        if cost >86:
            print(cost)
            
        visitedIndicator.add(state)
        
        if state.__resolvedState__():
            print("final", cost)
            for st in path:
                print(st)
            return

        for move_cost, move_to_state in state.__GetValidMovesAndCosts__():
            heapq.heappush(heap, (cost+move_cost, move_to_state, tuple(list(path) + [state])) )






def FindCheapestResolution(startConfigHall, startConfigRooms):
    
    currentState = Configuration(startConfigHall, startConfigRooms)
    currentCost  = 0
    heap = [(currentCost, currentState, ())]
    
    visitedConfigurations = set()
    
    while heap:
        cheapestAddition      = heapq.heappop(heap)
        cheapestCost          = cheapestAddition[0]
        cheapestConfiguration = cheapestAddition[1]
        cheapestPath          = cheapestAddition[2]
        
        if cheapestConfiguration in visitedConfigurations:
            continue
        
        visitedConfigurations.add(cheapestConfiguration)    
        
        print(cheapestCost)
        
        if cheapestConfiguration.__resolvedState__():
            print("Cheapest cost is :", cheapestCost)
            print("Path is:")
            for config in cheapestPath:
                print(config)
            return
            
        boundaryConfigs = cheapestConfiguration.__GetValidMovesAndCosts__()
        for boundary in boundaryConfigs:
            heapq.heappush(heap, (cheapestCost + boundary[0], boundary[1], tuple(list(cheapestPath) + [boundary[1]])))
            
        
    


class Configuration():
    def __init__(self, Hall, Rooms):
        self._hall = tuple([c for c in Hall])
        self._rooms =tuple([tuple([c for c in room]) for room in Rooms])
        
    
    def __repr__(self):
        hallString = "".join(["." if not c else c for c in self._hall])
        roomString = tuple("".join(["." if not c else c for c in room]) for room in self._rooms)
        return f"State(hall = {hallString}, rooms = {roomString})"

    def __hash__(self):
        return hash((self._hall, self._rooms))         

    def __eq__(self, otherConfig):
        return (self._hall, self._rooms) ==  (otherConfig._hall, otherConfig._rooms)  
    
    def __lt__(self, otherConfig):
        return repr(self) < repr(otherConfig)

    def __resolvedState__(self):
        return all([room[0] == correctOccupier and room[1] == correctOccupier and \
            room[2] == correctOccupier and room[3] == correctOccupier\
                for (room, correctOccupier) in zip(self._rooms, ["A", "B", "C", "D"])])     
            
    #Return cost and new Configuration.        
    def __GetValidMovesAndCosts__(self):
       
       returnList = []
       
       #Get moves into the Hall:
       returnList.extend(self.__GetMovesAndCostsIntoHall__())
           
       #Get moves into a room:    
       returnList.extend(self.__GetMovesAndCostsIntoRooms__())
           
       return sorted(returnList)    
       
                
    def __GetMovesAndCostsIntoHall__(self):
        
        returnList = []
        
        for i in range(4):
            
            nextRoom = self._rooms[i]
            if self.__IsNextRoomFixed__(i, nextRoom):
                continue
            else:
                (topLevel, topPod) = self.__GetTopLevelandTopPodInRoom__(nextRoom)
                
                #Moves Going Backwards First:
                firstPotentialLowerMove = 2*i +1
                while firstPotentialLowerMove >0 and self._hall[firstPotentialLowerMove] == None:
                    cost      = (abs(firstPotentialLowerMove - 2*i -2) + abs(0 - topLevel - 1))*costsDictionary[dictionaryPodIndices[topPod]]
                    #newConfig = Configuration(Hall = self._hall, Rooms = self._rooms)
                    newHall  = list(self._hall)
                    newRooms = [list(room) for room in self._rooms]
                    newRooms[i][topLevel]                    = None
                    newHall[firstPotentialLowerMove]         = topPod 
                    if topPod == None:
                        print(i)
                    check1 = sum(1 for x in newHall if x != None)
                    check2 = sum(sum(1 for x in room if x != None) for room in newRooms)
                    if check1 + check2 < 16:
                       print("error")
                    newConfig = Configuration(Hall = newHall, Rooms = newRooms)
                    returnList.append((cost, newConfig))
                    firstPotentialLowerMove -=2
                
                if firstPotentialLowerMove < 0 and self._hall[0] == None:
                    cost      = (abs(0 - 2*i -2) + abs(0 - topLevel -1))*costsDictionary[dictionaryPodIndices[topPod]]
                    #newConfig = Configuration(Hall = self._hall, Rooms = self._rooms)
                    newHall  = list(self._hall)
                    newRooms = [list(room) for room in self._rooms]
                    newRooms[i][topLevel]            = None
                    if topPod == None:
                        print(i)
                    newHall[0]                       = topPod 
                    check1 = sum(1 for x in newHall if x != None)
                    check2 = sum(sum(1 for x in room if x != None) for room in newRooms)
                    if check1 + check2 < 16:
                       print("error")
                    newConfig = Configuration(Hall = newHall, Rooms = newRooms)
                    returnList.append((cost, newConfig))
                    
                #Moves Going Forward in Hallway:  
                firstPotentialHigherMove = 2*i + 3
                while firstPotentialHigherMove < 10 and self._hall[firstPotentialHigherMove] == None:
                    cost      = (abs(firstPotentialHigherMove - 2*i - 2) + abs(0 - topLevel - 1))*costsDictionary[dictionaryPodIndices[topPod]]
                    #newConfig = Configuration(Hall = self._hall, Rooms = self._rooms)
                    newHall  = list(self._hall)
                    newRooms = [list(room) for room in self._rooms]
                    newRooms[i][topLevel]             = None
                    if topPod == None:
                        print(i)
                    newHall[firstPotentialHigherMove] = topPod 
                    check1 = sum(1 for x in newHall if x != None)
                    check2 = sum(sum(1 for x in room if x != None) for room in newRooms)
                    if check1 + check2 < 16:
                       print("error")
                    newConfig = Configuration(Hall = newHall, Rooms = newRooms)
                    returnList.append((cost, newConfig))
                    firstPotentialHigherMove +=2
                
                if firstPotentialHigherMove >10 and self._hall[10] == None:
                    cost      = (abs(10 - 2*i -2) + abs(0 - topLevel -1))*costsDictionary[dictionaryPodIndices[topPod]]
                    #newConfig = Configuration(Hall = self._hall, Rooms = self._rooms)
                    newHall  = list(self._hall)
                    newRooms = [list(room) for room in self._rooms]
                    newRooms[i][topLevel]            = None
                    if topPod == None:
                        print(i)
                    newHall[10]                      = topPod 
                    check1 = sum(1 for x in newHall if x != None)
                    check2 = sum(sum(1 for x in room if x != None) for room in newRooms)
                    if check1 + check2 < 16:
                       print("error")
                    newConfig = Configuration(Hall = newHall, Rooms = newRooms)
                    returnList.append((cost, newConfig))
                    
        return returnList              
                
                    
                          
    def __GetMovesAndCostsIntoRooms__(self):
        
        returnList = []
        
        for i in range(11):
            pod = self._hall[i]
            if pod == None:
                continue
                
            requiredRoomIndex = dictionaryPodIndices[pod]
            if 2*requiredRoomIndex + 2 > i:
                if any(self._hall[x] != None for x in range(i+1, 2*requiredRoomIndex + 3)):
                    continue
                if not self.__IsNextRoomFixed__(requiredRoomIndex, self._rooms[requiredRoomIndex]) :
                    continue
                    
                #Otherwise we can swap it in:
                (topLevel, _) = self.__GetTopLevelandTopPodInRoom__(self._rooms[requiredRoomIndex])
                if topLevel != 3 or (topLevel == 3 and self._rooms[requiredRoomIndex][3] != None):
                    topLevel-=1
                cost      = (abs(2*requiredRoomIndex + 2 - i) + abs(topLevel+1))*costsDictionary[requiredRoomIndex]
                #newConfig = Configuration(Hall = self._hall, Rooms = self._rooms)
                newHall  = list(self._hall)
                newRooms = [list(room) for room in self._rooms]
                newRooms[requiredRoomIndex][topLevel]            = pod
                newHall[i]                                       = None 
                check1 = sum(1 for x in newHall if x != None)
                check2 = sum(sum(1 for x in room if x != None) for room in newRooms)
                if check1 + check2 < 16:
                    print("error")
                newConfig = Configuration(Hall = newHall, Rooms = newRooms)
                returnList.append((cost, newConfig))
                
                
                
            if 2*requiredRoomIndex + 2 < i:
                if any(self._hall[x] != None for x in range(2*requiredRoomIndex + 2, i)):
                    continue
                if not self.__IsNextRoomFixed__(requiredRoomIndex, self._rooms[requiredRoomIndex]) :
                    continue
                    
                #Otherwise we can swap it in:
                (topLevel, _) = self.__GetTopLevelandTopPodInRoom__(self._rooms[requiredRoomIndex])
                if topLevel != 3 or (topLevel == 3 and self._rooms[requiredRoomIndex][3] != None):
                    topLevel-=1
                cost      = (abs(2*requiredRoomIndex + 2 - i) + abs(topLevel+1))*costsDictionary[requiredRoomIndex]
                #newConfig = Configuration(Hall = self._hall, Rooms = self._rooms)
                newHall  = list(self._hall)
                newRooms = [list(room) for room in self._rooms]
                newRooms[requiredRoomIndex][topLevel]            = pod
                newHall[i]                                       = None 
                check1 = sum(1 for x in newHall if x != None)
                check2 = sum(sum(1 for x in room if x != None) for room in newRooms)
                if check1 + check2 < 16:
                    print("error")
                newConfig = Configuration(Hall = newHall, Rooms = newRooms)
                returnList.append((cost, newConfig))  
                
            
        return returnList        
                
                
        
    def __GetTopLevelandTopPodInRoom__(self, room):
        topIndex = 0
        while topIndex < 3 and room[topIndex] == None:
            topIndex +=1
        
        return topIndex, room[topIndex]    
            

    def __IsNextRoomFixed__(self, roomIndex, room):
        if any(x in (set(podIndices) - set([podIndices[roomIndex]])) for x in room):
               return False
        else:
            return True    
        
#Test:
hall = [None for i in range(11)]
#hall[0] = "A"
rooms = [["B", "D", "D", "D"], ["B", "C", "B", "A"], ["C", "B", "A", "A"], ["D", "A", "C", "C"]]

config = Configuration(hall, rooms)

#Solution Part 1 solved by hand.

#Solution Part 2
print(FindCheapestResolution(hall, rooms))  
#print(config.__resolvedState__())  