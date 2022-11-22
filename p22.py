# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:35:36 2022

@author: Padraig
"""

#file path: "C:\Users\Padraig\Desktop\desktop\AdventOfCode\p22\p22.txt"


class Cube:
    
    def __init__(self, x1,x2,y1,y2,z1,z2):
        #For a technical reason that needs better handling if we initialise an x or y coordinate
        # None, we just replace it by the other x or y coordinate.
        if x1 == None:
            x1 = x2
            
        if x2 == None:
            x2 = x1   
            
        if y1 == None:
            y1 = y2
            
        if y2 == None:
            y2 = y1
            
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        
    def __repr__(self):
        return f"({self.x1}->{self.x2}, {self.y1}->{self.y2}, {self.z1}->{self.z2})"


    def __hash__(self):
        return hash((self.x1, self.x2, self.y1, self.y2, self.z1, self.z2))
  
    def Volume(self):
       return (self.x2-self.x1 +1)*(self.y2-self.y1+1)*(self.z2-self.z1+1)
   

def LoadAndProcessInput(stringPath):
      
    switchInstructions = []
    listOfCubes       = []
    file = open(stringPath)
    for line in file:
        firstSplit = line.split(" ")
        switchInstructions.append(firstSplit[0])
        secondSplit = firstSplit[1].split(",")
        
        thirdSplit  = secondSplit[0].split("=")
        fourthSplit = thirdSplit[1].split("..")
        x1 = fourthSplit[0]
        x2 = fourthSplit[1]
        
        thirdSplit  = secondSplit[1].split("=")
        fourthSplit = thirdSplit[1].split("..")
        y1 = fourthSplit[0]
        y2 = fourthSplit[1]
        
        thirdSplit  = secondSplit[2].split("=")
        fourthSplit = thirdSplit[1].split("..")
        z1 = fourthSplit[0]
        z2 = fourthSplit[1]
        
        listOfCubes.append(Cube(int(x1),int(x2),int(y1),int(y2),int(z1),int(z2)))
        
    return switchInstructions, listOfCubes    


def GetIntersectionPattern(c1x1, c1x2, c2x1, c2x2):
    """Gets the intersection pattern between two cubes c1 and c2 for a given dimension"""

    #iX
    if c2x1 < c1x1 and c2x2 < c1x1:
        iX = [c2x1, None, None, c2x2]
            
    elif c2x1 < c1x1 and c2x2 == c1x1: 
        iX = [c2x1, c2x2, None, None]
        
    elif c2x1 < c1x1 and c2x2 > c1x1 and c2x2 < c1x2:
        iX = [c2x1, c1x1, c2x2, None]
        
    elif c2x1 < c1x1 and c2x2 > c1x1 and c2x2 == c1x2:
        iX = [c2x1, c1x1, c2x2, None]
        
    elif  c2x1 < c1x1 and c2x2 > c1x1 and c2x2 > c1x2:   
        iX = [c2x1, c1x1, c1x2, c2x2]
     
        
    elif  c2x1 == c1x1 and  c2x2 < c1x2:   
        iX = [None, c1x1,  c2x2, None]
        
    elif  c2x1 == c1x1 and  c2x2 == c1x2:   
        iX = [None, c1x1, c2x2, None]
     
    elif  c2x1 == c1x1 and  c2x2 > c1x2:   
        iX = [None, c1x1, c1x2, c2x2]  
        
    elif  c2x1 > c1x1  and c2x1 < c1x2 and  c2x2 <= c1x2:   
        iX = [None, c2x1, c2x2, None]      
        
    elif  c2x1 > c1x1  and c2x1 < c1x2 and  c2x2 > c1x2:   
        iX = [None, c2x1, c1x2, c2x2]        
        
    elif  c2x1 == c1x2:   
        iX = [None, None, c2x1, c2x2]
            
    elif c2x1 > c1x2:
        iX = [c2x1, None, None, c2x2]
        
    return iX    


def ResolveAdditionalCubes(c1, c2):
    """ c1 is the base: we return the additional cubes from that c2 cube that do not overlap with c1"""
    additionalCubes = []
    
    iX = GetIntersectionPattern(c1.x1, c1.x2, c2.x1, c2.x2)
    iY = GetIntersectionPattern(c1.y1, c1.y2, c2.y1, c2.y2)
    iZ = GetIntersectionPattern(c1.z1, c1.z2, c2.z1, c2.z2)
    
    
    if (iX[1] == None and iX[2] == None) or (iY[1] == None and iY[2] == None) or ((iZ[1] == None and iZ[2] == None)):
        additionalCubes.append(c2)
        return additionalCubes
    else:
        
       #Left Outside 
       if (iX[0] != None and iX[1] != None):
           additionalCubes.append(Cube(iX[0], iX[1]-1, c2.y1, c2.y2, c2.z1, c2.z2))
               
        #Right Outside
       if (iX[2] != None and iX[3] != None):       
           additionalCubes.append(Cube(iX[2]+1, iX[3], c2.y1, c2.y2, c2.z1, c2.z2))
               
       #Intersection:
       if (iX[1] != None or iX[2] != None):
           
           #Y Intersections:
               #Left Outside 
               if (iY[0] != None and iY[1] != None):
                   additionalCubes.append(Cube(iX[1], iX[2], iY[0], iY[1]-1,  c2.z1, c2.z2))
                       
                #Right Outside
               if (iY[2] != None and iY[3] != None):       
                   additionalCubes.append(Cube(iX[1], iX[2], iY[2]+1, iY[3],  c2.z1, c2.z2))
                   
               #Intersections:
               if (iY[1] != None or iY[2] != None):
                       
                     #Z Intersections:
                         #Left Outside 
                         if (iZ[0] != None and iZ[1] != None):
                             additionalCubes.append(Cube(iX[1], iX[2], iY[1], iY[2],  iZ[0], iZ[1]-1))
                                 
                          #Right Outside
                         if (iZ[2] != None and iZ[3] != None):       
                             additionalCubes.append(Cube(iX[1], iX[2], iY[1], iY[2],  iZ[2]+1, iZ[3])) 
                             
    return additionalCubes                        
                                         

#Assumes first cube will be "on"                       
def CalculateFinalVolume(instructions, cubes):
    cubeCache = []
    cubeCache.append(cubes[0])
    
    for i in range(1, len(cubes)):
        if instructions[i] == "on":
            
            nextCube = cubes[i]
            cubesToAdd = [nextCube]
            for c in cubeCache:
                    #These will be disjoint.
                    cubesToAdd +=  ResolveAdditionalCubes(nextCube, c)
            cubeCache = list(set(cubesToAdd))        
                    
        if instructions[i] == "off":
            nextCube = cubes[i]
            cubesToAdd = []
            for c in cubeCache:
                    #These will be disjoint.
                    cubesToAdd += ResolveAdditionalCubes(nextCube, c)
            cubeCache = list(set(cubesToAdd))
            
        totalVolume = 0
        for c in cubeCache:
            totalVolume+=c.Volume()
    return totalVolume    
            

#Part 1:

    
def CalculateFinalVolumePart1(instructions, cubes):
    cubeCache = []
    cubeCache.append(cubes[0])
    
    for i in range(1, len(cubes)):
        if (cubes[i].x1 < -50 or cubes[i].x1 > 50 \
            or cubes[i].x2 < -50 or cubes[i].x2 > 50 \
            or cubes[i].y1 < -50 or cubes[i].y1 > 50 \
            or cubes[i].y2 < -50 or cubes[i].y2 > 50 \
            or cubes[i].z1 < -50 or cubes[i].z1 > 50 \
            or cubes[i].z2 < -50 or cubes[i].z2 > 50):
            continue
        
        if instructions[i] == "on":
            
            nextCube = cubes[i]
            cubesToAdd = [nextCube]
            for c in cubeCache:
                    #These will be disjoint.
                    cubesToAdd +=  ResolveAdditionalCubes(nextCube, c)
            cubeCache = list(set(cubesToAdd))        
                    
        if instructions[i] == "off":
            nextCube = cubes[i]
            cubesToAdd = []
            for c in cubeCache:
                    #These will be disjoint.
                    cubesToAdd += ResolveAdditionalCubes(nextCube, c)
            cubeCache = list(set(cubesToAdd))
            
        totalVolume = 0
        for c in cubeCache:
            totalVolume+=c.Volume()
    return totalVolume   
            
#ResolveAdditionalCubes(Cube(11,13,11,13,11,13), Cube(10,12,10,12,10,12))            
switchInstructions, listOfCubes = LoadAndProcessInput(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p22\p22.txt")    
print("Solution Part 1: ", CalculateFinalVolumePart1( switchInstructions, listOfCubes))        
print("Solution Part 2: ", CalculateFinalVolume( switchInstructions, listOfCubes) )





                       
 
                   
#c1 = Cube(-10,10,-10,10,-10,10)                  
#c2 = Cube(-20,20,-10,10,-20,20)                 
#ResolveAdditionalCubes(c1, c2)                       
           
               
               
           
        
    
    
    
        
        