# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:14:31 2021

@author: Padraig
"""

#p1 starts on 4
#p2 start on 9
import numpy as np

def PlayerRoll(diceTotal, startPosition):
    endPosition = startPosition + (diceTotal)%10
    if endPosition >10:
        endPosition = endPosition%10
    return endPosition


def RollDicePart1(iteration):
    return ((iteration*3)%100 + 1) + ((iteration*3)%100 + 2) + ((iteration*3)%100 + 3)


def simulatePart1(start1, start2):
    iteration = 0
    p1Total   = 0
    p2Total   = 0
    
    while p1Total < 1000 and p2Total<1000:
        start1 = PlayerRoll(RollDicePart1(iteration), start1)
        p1Total += start1
        iteration += 1
        
        if p1Total >= 1000:
            break
        
        
        start2 = PlayerRoll(RollDicePart1(iteration), start2)
        p2Total += start2
        iteration += 1
        
        if p2Total >= 1000:
            break
            
        
        
        print(p1Total, p2Total)
        
    if p1Total >=1000:
        print(iteration, p2Total)
        return 3*iteration*p2Total
    
    else:
        print(iteration, p1Total)
        return 3*iteration*p1Total
            
        
    

def IterateNextTurns(stateMatrix):
    nextStateMatrix  = np.zeros((21,11, 21, 11))
    p1WinsTurn       = 0
    p2WinsTurn       = 0
    
    for i in range(21):
        for j in range(11):
            for ii in range(21):
                for jj in range(11):
                    if i + PlayerRoll(j, 3) > 20:
                        p1WinsTurn += stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i + PlayerRoll(j, 3), PlayerRoll(j, 3), ii, jj]+= stateMatrix[i,j, ii, jj]
                        
                    if i + PlayerRoll(j, 4) > 20:
                        p1WinsTurn += 3*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i + PlayerRoll(j, 4), PlayerRoll(j, 4), ii, jj]+= 3*stateMatrix[i,j, ii, jj] 
                        
                    if i + PlayerRoll(j, 5) > 20:
                        p1WinsTurn += 6*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i + PlayerRoll(j, 5), PlayerRoll(j, 5), ii, jj]+= 6*stateMatrix[i,j, ii, jj] 
                        
                        
                    if i + PlayerRoll(j, 6) > 20:
                        p1WinsTurn += 7*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i + PlayerRoll(j, 6), PlayerRoll(j, 6), ii, jj]+= 7*stateMatrix[i,j, ii, jj]     
                
                    if i + PlayerRoll(j, 7) > 20:
                        p1WinsTurn += 6*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i + PlayerRoll(j, 7), PlayerRoll(j, 7), ii, jj]+= 6*stateMatrix[i,j, ii, jj] 
                        
                    if i + PlayerRoll(j, 8) > 20:
                        p1WinsTurn += 3*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i + PlayerRoll(j, 8), PlayerRoll(j, 8), ii, jj]+= 3*stateMatrix[i,j, ii, jj]     

                    if i + PlayerRoll(j, 9) > 20:
                        p1WinsTurn += stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i + PlayerRoll(j, 9), PlayerRoll(j, 9), ii, jj]+= stateMatrix[i,j, ii, jj] 
    
    stateMatrix     = nextStateMatrix.copy()                    
    nextStateMatrix = np.zeros((21,11, 21, 11))       
    for i in range(21):
        for j in range(11):
            for ii in range(21):
                for jj in range(11):
                    
                    if ii + PlayerRoll(jj, 3) > 20:
                        p2WinsTurn += stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i,j,ii + PlayerRoll(jj, 3), PlayerRoll(jj, 3)]+= stateMatrix[i,j, ii, jj]
                        
                    if ii + PlayerRoll(jj, 4) > 20:
                        p2WinsTurn += 3*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i,j,ii + PlayerRoll(jj, 4), PlayerRoll(jj, 4)]+= 3*stateMatrix[i,j, ii, jj] 
                        
                    if ii + PlayerRoll(jj, 5) > 20:
                        p2WinsTurn += 6*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i,j,ii + PlayerRoll(jj, 5), PlayerRoll(jj, 5)]+= 6*stateMatrix[i,j, ii, jj] 
                        
                        
                    if ii + PlayerRoll(jj, 6) > 20:
                        p2WinsTurn += 7*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i, j,ii + PlayerRoll(jj, 6), PlayerRoll(jj, 6)]+= 7*stateMatrix[i,j, ii, jj]     
                
                    if ii + PlayerRoll(jj, 7) > 20:
                        p2WinsTurn += 6*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i, j, ii + PlayerRoll(jj, 7), PlayerRoll(jj, 7)]+= 6*stateMatrix[i,j, ii, jj] 
                        
                    if ii + PlayerRoll(jj, 8) > 20:
                        p2WinsTurn += 3*stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i, j, ii + PlayerRoll(jj, 8), PlayerRoll(jj, 8)]+= 3*stateMatrix[i,j, ii, jj]     

                    if ii + PlayerRoll(jj, 9) > 20:
                        p2WinsTurn += stateMatrix[i,j, ii, jj]
                    else:
                        nextStateMatrix[i, j,ii + PlayerRoll(jj, 9), PlayerRoll(jj, 9)]+= stateMatrix[i,j, ii, jj] 
    print("Processed Iteration")                    
    return p1WinsTurn, p2WinsTurn, nextStateMatrix                                                

def SolvePart2(start1, start2):
    stateMatrix = np.zeros((21,11, 21, 11))
    stateMatrix[0, start1, 0, start2] = 1
    
    p1Wins = 0
    p2Wins = 0
    
    while sum(np.sum(np.sum(np.sum(stateMatrix, axis =1), axis =1), axis=1)) !=0:
        print(sum(np.sum(np.sum(np.sum(stateMatrix, axis =1), axis =1), axis=1)))
        p1WinsOnNextTurn, p2WinsOnNextTurn, stateMatrix = IterateNextTurns(stateMatrix)
        
        p1Wins+=p1WinsOnNextTurn
        p2Wins+=p2WinsOnNextTurn
        
    if p1Wins> p2Wins:
        return p1Wins
    else:
        return p2Wins
        
print("Solution Part 1: ", simulatePart1(4,9))        
print("Solution Part 2:", SolvePart2(4, 9))        
    