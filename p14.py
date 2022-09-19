# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:48:01 2021

@author: pcondon
"""
import numpy as np

from collections import Counter
file = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p14\p14.txt", 'r')
startLine = file.readline()
startLine = startLine.strip()

file.readline()

insertionRules = {}
line = file.readline()
while line.strip():
    line = line.strip().split(" -> ")
    insertionRules[line[0]] = line[1]
    line = file.readline()


def BuildPart1(inputString, insertionRules, iterations):
    for i in range(iterations):
        #print(i)
        initialLength = len(inputString)
        for j in range(initialLength-2, -1, -1):
            inputString = inputString[0: j+1] + insertionRules[inputString[j: j+2]] + inputString[j+1:]
        
    return inputString;        


#print( BuildPart1(startLine, insertionRules, 1))
counter = Counter(BuildPart1(startLine, insertionRules, 10))
print ("Solution Part 1:", max(counter.values()) - min(counter.values()))


def BuildGeneratorDictionary(insertionRules):
    generatorDictionary = {}
    for primeKey in insertionRules.keys():
        nextGeneratorSet = []
        for key in insertionRules.keys():
            test1 = key[0] + insertionRules[key]
            test2 = insertionRules[key] + key[1]
            if test1 == primeKey:
                nextGeneratorSet.append(key)
            if test2 == primeKey:    
                nextGeneratorSet.append(key)
        
        nextGeneratorSet = set(nextGeneratorSet)
        generatorDictionary[primeKey] = nextGeneratorSet        
            
    return generatorDictionary


def BuildKeyIndexMap(insertionRules):
    indexKeyDictionary = {}
    counter = 0
    for key in insertionRules.keys():
        indexKeyDictionary[key] = counter
        counter +=1
    return indexKeyDictionary


def FillInitialLineInCountTable(countTable, indexKeyDictionary, startLine):
    
    for i in range(0, len(startLine)-1):
        countTable[0, indexKeyDictionary[startLine[i:i+2]]]+=1
    return countTable


def ProcessIterationInCountTable(countTable, indexKeyDictionary, generatorDictionary, iteration):
    for key in indexKeyDictionary:
        keyCount = 0
        for value in generatorDictionary[key]:
            keyCount += countTable[iteration-1, indexKeyDictionary[value]]
            
        countTable[iteration, indexKeyDictionary[key]] = keyCount
    return countTable        
        
 
        
def ReturnTotals(indexKeyDictionary, countTable, iteration):
    countDictionary = {}
    for key in indexKeyDictionary.keys():
        countDictionary[key[0]] = 0
        countDictionary[key[1]] = 0
        
    for key in indexKeyDictionary.keys():
        countDictionary[key[0]] += countTable[iteration, indexKeyDictionary[key]]
        countDictionary[key[1]] += countTable[iteration, indexKeyDictionary[key]]
        
    return countDictionary


indexKeyDictionary  = BuildKeyIndexMap(insertionRules)
generatorDictionary = BuildGeneratorDictionary(insertionRules)

countTable = np.zeros((41, len(indexKeyDictionary.keys())))
countTable = FillInitialLineInCountTable(countTable, indexKeyDictionary, startLine)
#print(countTable)
for i in range(1, 41):
    countTable = ProcessIterationInCountTable(countTable, indexKeyDictionary, generatorDictionary, i)
    
    

answerDictionary = ReturnTotals(indexKeyDictionary, countTable, 40)
T1 = max(answerDictionary, key=answerDictionary.get)
T2 = min(answerDictionary, key=answerDictionary.get) 

print("Solution Part 2:", (answerDictionary[T1])/2 - (answerDictionary[T2]+2)/2)  





