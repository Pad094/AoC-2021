# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 08:48:49 2021

@author: pcondon
"""
#a = (
#b = [
#c = { 
#d = <


testData = []
inputFile = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p10\p10.txt", 'r')
inputFile = inputFile.readlines()
for line in inputFile:
    line = str(line).strip()
    testData.append(list(line))

def CheckIfInvalid(line):
    trackerDictionary = {}
    trackerDictionary["("] = 0
    trackerDictionary["["] = 0
    trackerDictionary["{"] = 0
    trackerDictionary["<"] = 0
    
    for character in line:
        if character == "(":
            trackerDictionary["("] += 1
        if character == ")":
            trackerDictionary["("] -= 1
        if character == "[":
            trackerDictionary["["] += 1
        if character == "]":
            trackerDictionary["["] -= 1
        if character == "{":
            trackerDictionary["{"] += 1
        if character == "}":
            trackerDictionary["{"] -= 1
        if character == "<":
            trackerDictionary["<"] += 1
        if character == ">":
            trackerDictionary["<"] -= 1    
            
        if min(trackerDictionary["("],trackerDictionary["["],trackerDictionary["{"],trackerDictionary["<"]) <0:      
            return character
            break
        
    return "!";   


def CheckIfInvalidStack(line):
    stack = []
    
    for character in line:
     
        if character == "(":
            stack.append(")")
        if character == ")":
            if not character == stack.pop():
                return character
                break
                
        if character == "[":
             stack.append("]")
        if character == "]":
             if not character == stack.pop():
                 return character
                 break
                 
        if character == "{":
            stack.append("}")
        if character == "}":
            if not character == stack.pop():
                return character
                break
                
        if character == "<":
            stack.append(">")
        if character == ">":
            if not character == stack.pop():
                return character
                break
            
                
    return stack           

    

#testData = [["{", "(", "[", "(", "<", "{", "}", "[", "<", ">", "[", "]", "}", ">", "{", "[", "]", "{","[",  "(", "<", "(", ")", ">"]];

def Part1Solution(testData):
    
    solutionTotal = 0
    for line in testData:
        character = CheckIfInvalidStack(line)
        if character == "(" or character == ")":
            solutionTotal += 3
        if character == "[" or  character =="]":
            solutionTotal += 57
        if character == "{" or character == "}":
            solutionTotal += 1197
        if character == "<" or character == ">":
            solutionTotal += 25137;    
            
    return solutionTotal;        
            
   
def CheckIfIncomplete(line):
    character = CheckIfInvalidStack(line)
    if  not isinstance(character, list): 
        return False
    
    return True

def ResolveStack(stack):
    resultant = 0
    while len(stack)>0:
        character = stack.pop()
        resultant*=5
        if character == "(" or character == ")":
            resultant += 1
        if character == "[" or  character =="]":
            resultant += 2
        if character == "{" or character == "}":
            resultant += 3
        if character == "<" or character == ">":
            resultant += 4    
    return resultant;    
   
def Part2Solution(testData):
    IncompleteTotals = []
    for line in testData:
        if CheckIfIncomplete(line):
            IncompleteTotals.append(ResolveStack( CheckIfInvalidStack(line)))
    
    IncompleteTotals.sort()      
    midPoint = int((len(IncompleteTotals)-1)/2)
    return IncompleteTotals[midPoint]         
           
#print(len(testData))      
print(Part1Solution(testData))  
print(Part2Solution(testData))