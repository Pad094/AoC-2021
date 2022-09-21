# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:38:56 2022

@author: Padraig
"""

import numpy as np
import copy
# "C:\Users\Padraig\Desktop\desktop\AdventOfCode\p19\p19.txt"
def LoadAndProcessData(filePath):
    scannerCount = 0
    ScannerSet = []
    with open(filePath) as file:
        for line in file:
            if line[0] == "-" and line[1] == "-": #New Scanner
                nextCoordinates = []
                
            elif not line.strip():
                #nextCoordinates = np.array(nextCoordinates)
                ScannerSet.append(Scanner(nextCoordinates, scannerCount))
                scannerCount +=1
                
            else:
                nextCoordinates.append(tuple([int(x) for x in line.split(",")]))
    
    ScannerSet.append(Scanner(nextCoordinates, scannerCount))
    return ScannerSet             
            

class Scanner:
    def __init__(self, coordinates, ID):
        self._ID = ID
        self._coordinates = coordinates
        self._origin = [0,0,0]
        self._isNormalised = False
        self._transformed_coordinates = list(coordinates)
        self._transformed_origin = [0,0,0]
        
        
    def __repr__(self):
        return "Scanner: " + str(self._ID)
    
    def __hash__(self):
        return self._ID
    
    def Transform(self, NewOrigin, transformID):
        self._transformed_origin = NewOrigin
        for i in range(len(self._coordinates)):
            self._transformed_coordinates[i] = TransformCoordinate(self._coordinates[i], self._transformed_origin, transformID)
            
        
    
  
def ReturnRelativeOrigin(coordinateBase, coordinateAlternate, transformID): 
     coordinateBase = np.array(coordinateBase)
     xa = coordinateAlternate[0]
     ya = coordinateAlternate[1]
     za = coordinateAlternate[2]
     
     if transformID == 0:
         # x,y,z, +,+,+
         return coordinateBase - np.array(coordinateAlternate)
     
     elif transformID ==1:
         # x,y,z, -,-,+
         return coordinateBase - np.array([-xa,-ya,za])
     
     elif transformID ==2:
            # x,y,z, -,+,-1
            return coordinateBase - np.array([-xa,ya,-za])
        
     elif transformID ==3:
            # x,y,z, -,+,-1
            return coordinateBase - np.array([xa,-ya,-za])   
     
     #Swap x and y   
     elif transformID == 4:
         # y,x,z, +,+,+
         return coordinateBase - np.array([-ya,xa,za]) 
     
     elif transformID ==5:
         # x,y,z, -,-,+
         return coordinateBase - np.array([ya,-xa,za])
     
     elif transformID ==6:
            # x,y,z, -,+,-1
            return coordinateBase - np.array([-ya,-xa,-za])
        
     elif transformID ==7:
            # x,y,z, -,+,-1
            return coordinateBase - np.array([ya,xa,-za])      
     
        
     
      #Swap x and z   
     elif transformID == 8:
          # y,x,z, +,+,+
          return coordinateBase - np.array([za,ya,-xa]) 
      
     elif transformID ==9:
          # x,y,z, -,-,+
          return coordinateBase - np.array([-za,-ya,-xa])
      
     elif transformID ==10:
             # x,y,z, -,+,-1
             return coordinateBase - np.array([-za,ya,xa])
         
     elif transformID ==11:
             # x,y,z, -,+,-1
             return coordinateBase - np.array([za,-ya,xa])    
         
            
         
            
     #Swap y and z   
     elif transformID == 12:
         # y,x,z, +,+,+
         return coordinateBase - np.array([xa,za,-ya]) 
     
     elif transformID ==13:
         # x,y,z, -,-,+
         return coordinateBase - np.array([-xa,-za,-ya])
     
     elif transformID ==14:
            # x,y,z, -,+,-1
            return coordinateBase - np.array([-xa,za,ya])
        
     elif transformID ==15:
            # x,y,z, -,+,-1
            return coordinateBase - np.array([xa,-za,ya])    
        
        
    # Swap to (y,z,x)
     elif transformID == 16:
            # y,x,z, +,+,+
            return coordinateBase - np.array([ya,za,xa]) 
        
     elif transformID ==17:
            # x,y,z, -,-,+
            return coordinateBase - np.array([-ya,-za,xa])
        
     elif transformID ==18:
               # x,y,z, -,+,-1
               return coordinateBase - np.array([-ya,za,-xa])
          
     elif transformID ==19:
               # x,y,z, -,+,-1
               return coordinateBase - np.array([ya,-za,-xa])      
        
        
        
    # Swap to (z,x,y)
     elif transformID == 20:
        # y,x,z, +,+,+
        return coordinateBase - np.array([za,xa,ya]) 
    
     elif transformID ==21:
        # x,y,z, -,-,+
        return coordinateBase - np.array([-za,-xa,ya])
    
     elif transformID ==22:
           # x,y,z, -,+,-1
           return coordinateBase - np.array([-za,xa,-ya])
       
     elif transformID ==23:
           # x,y,z, -,+,-1
           return coordinateBase - np.array([za,-xa,-ya])    
       
        
       
def TransformCoordinate(oldCoordinate, newOrigin, TransformID):
    
    transformedCoordinate =  ReturnRelativeOrigin(newOrigin, -np.array(oldCoordinate), TransformID)
    transformedCoordinate = tuple(transformedCoordinate)
    return transformedCoordinate

def NormaliseScannerPair(BaseScanner, AlternateScanner):
     #Pair each beacon combo between Base and Alternate:
     #Back out origin each time:
     #Check if 6 beacons match. Break if so.
     for i in range(len(BaseScanner._coordinates) -10):
         for j in range(len(AlternateScanner._coordinates)):
             for k in range(24):
                 #print(i)
                 #scanner2 = copy.deepcopy(AlternateScanner)
                 if AlternateScanner._coordinates[0][0] != 686:
                     pass
                 potentialOrigin = ReturnRelativeOrigin(BaseScanner._coordinates[i], AlternateScanner._coordinates[j], k)
                 if AlternateScanner._coordinates[0][0] != 686:
                     pass
                 
                 if BaseScanner._coordinates[i][0] == -618:
                     pass
                 if BaseScanner._coordinates[i][0] == -618 and AlternateScanner._coordinates[j][0] ==686:
                     pass
                 
                 AlternateScanner.Transform(potentialOrigin, k)
                 if AlternateScanner._coordinates[0][0] != 686:
                     pass
                 if len(set(BaseScanner._coordinates).intersection(set(AlternateScanner._transformed_coordinates))) >11 and AreTransformedCoordinatesWithinRange(AlternateScanner):
                     AlternateScanner._coordinates = AlternateScanner._transformed_coordinates
                     AlternateScanner._origin = AlternateScanner._transformed_origin
                     return AlternateScanner
     return None            

def AreTransformedCoordinatesWithinRange(Scanner):
    output = True
    for i in range(len(Scanner._coordinates)):    
        for j in range(3):
            if abs(Scanner._transformed_coordinates[i][j] - Scanner._transformed_origin[j]) >1000:
                output = False
                break
    return output        
                
                 

def NormaliseAllScanners(ScannerSet):
      numberOfScanners = len(ScannerSet)
      ScannerSet[0]._isNormalised = True
      NormalisedScannerSet = []
      
      normalisedCount = 0
      while normalisedCount < numberOfScanners:
      #Get next normalised Scanner:
          for i in range(len(ScannerSet)):
              if ScannerSet[i]._isNormalised == True:
                  break 
           
          NormalisedScannerSet.append(ScannerSet[i])   
          normalisedCount+=1
          if normalisedCount == 2:
              pass
          
          print(normalisedCount)
          del ScannerSet[i]
          for j in range(len(ScannerSet)):
              if ScannerSet[j]._isNormalised == False:
                  potentialNormalisedScannner = NormaliseScannerPair(NormalisedScannerSet[-1], ScannerSet[j])
                  if potentialNormalisedScannner == None:
                      continue
                  else:
                      ScannerSet[j] = potentialNormalisedScannner
                      ScannerSet[j]._isNormalised = True
                      
  
      return NormalisedScannerSet               
      

def SolvePart1(filepath):
    ScannerSet = LoadAndProcessData(filepath)    
    NormalisedScannerSet = NormaliseAllScanners(ScannerSet)
    beaconSet = set([])
    for i in NormalisedScannerSet:
        for j in range(len(i._coordinates)):
            beaconSet.add(i._coordinates[j])
    print("Solution Part 1:",  len(beaconSet))        
    return NormalisedScannerSet#len(beaconSet)  

    
def SolvePart2(filepath):
    ScannerSet = SolvePart1(filepath)
    beaconSet = set([])
    for i in ScannerSet:
            beaconSet.add(tuple(i._origin))
    beaconSet = list(beaconSet)
    maxDistance = 0
    for i in range(len(beaconSet)-1):
        for j in range(i+1, len(beaconSet)):
            #maxDistance = max(maxDistance,GetMaxDistance(beaconSet[i], beaconSet[j]) )
            if GetMaxDistance(beaconSet[i], beaconSet[j]) > maxDistance:
                maxDistance = GetMaxDistance(beaconSet[i], beaconSet[j])
    #print(maxDistance)            
    return maxDistance        
            
    
def GetMaxDistance(coordinates1, coordinates2):
    return abs(coordinates1[0] - coordinates2[0]) + abs(coordinates1[1] - coordinates2[1]) + abs(coordinates1[2] - coordinates2[2])            
    
       
   
#def SolveTest():
print("Solution Part 1:", SolvePart1(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p19\p19.txt"))
       
      
print("Solution Part 2:", SolvePart2(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p19\p19.txt") )
   
        