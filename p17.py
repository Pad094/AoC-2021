# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 08:48:35 2021

@author: pcondon
"""
def GetValidTimesForGivenY(y, ylowerBound, yUpperBound):
    
    potentialTimes = []
    currentY       = 0
    time           = 0
    
    
    while currentY >= ylowerBound:
        if currentY <= yUpperBound:
            potentialTimes.append(time)
                    
        currentY += (y - time) 
        time +=1
        
        
    return potentialTimes


def XCoordinateAfterTimeT(x, time):
    timeCount   = 0
    xCoordinate = 0
    while timeCount < time:
        xCoordinate += max(x - timeCount, 0)
        timeCount +=1
    
    return xCoordinate            

def IsThereValidXForPotentialTimes(potentialTimes, xLowerBound, xUpperBound):  
    for time in potentialTimes:
        x = 1
        
        while x < xUpperBound:
            if XCoordinateAfterTimeT(x, time) >= xLowerBound and  XCoordinateAfterTimeT(x, time) <= xUpperBound:
                return True
            
            else:
                x+=1
    return False           
         
                
#print(IsThereValidXForPotentialTimes([8], 20, 30))


def GetMaxYValue(xlower, xupper, ylower, yupper):
    
    maxPotentialY = abs(ylower)
  
    
    while maxPotentialY >0:
        nextTimes = GetValidTimesForGivenY(maxPotentialY, ylower, yupper)
        if IsThereValidXForPotentialTimes(nextTimes, xlower, xupper):
                return maxPotentialY
        else:
                maxPotentialY-=1
    return 0            
            
maxy = GetMaxYValue(85, 145, -163, -108)
print("Solution Part 1:", maxy*(maxy+1)/2)   

def GetAllValidXCoordinates(potentialTimes, xLowerBound, xUpperBound):  
   
   validXCoordinates = [] 
   for time in potentialTimes:
        x = 0
        
        while x <= xUpperBound:
            if XCoordinateAfterTimeT(x, time) >= xLowerBound and  XCoordinateAfterTimeT(x, time) <= xUpperBound:
                validXCoordinates.append(x)
            x+=1    
            
            
   return validXCoordinates 



def GetAllCoordinatePairs(xlower, xupper, ylower, yupper):
    
    allCoordinatePairs = []
    maxPotentialY = abs(ylower)
    
    while maxPotentialY  >= -  abs(ylower):
        nextTimes = GetValidTimesForGivenY(maxPotentialY, ylower, yupper)
        validXCoordinates =  GetAllValidXCoordinates(nextTimes, xlower, xupper)
        if len(validXCoordinates) >0:
            for xCoord in validXCoordinates:
                allCoordinatePairs.append([xCoord, maxPotentialY])
                 
        maxPotentialY-=1
    return allCoordinatePairs       

startVelocities = GetAllCoordinatePairs(85,145,-163,-108)

#print(startVelocities)
print("Solution Part 2:", len(set(map(tuple, startVelocities))))
