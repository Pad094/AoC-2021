# -*- coding: utf-8 -*-
"""
Created on Sun May  1 11:11:56 2022

@author: Padraig
"""
import math

def LoadInData(stringPath):
    rows = []
    with open(stringPath) as file:
        for row in file:
            rows.append(row)
    return rows     

    
class Tree:
    def __init__(self, root):
        self.root  = root
        self.root.nodeDepth = 0 # For technical reasons
        self.nodes = dict()
        self.nodes[0] = root
    
    def __repr__(self):
        return "Root node: " + str(self.root)
        
    def AddNode(self, newNode, parentNode, leftChild, newNodeValue):
        self.nodes[newNode.index] = newNode
        self.nodes[newNode.index].parent = parentNode.index
        if newNodeValue != None:
            self.nodes[newNode.index].nodeValue = newNodeValue            
        if leftChild ==1:
            self.nodes[parentNode.index].leftChild = newNode.index
        else:
            self.nodes[parentNode.index].rightChild = newNode.index
            
        self.nodes[newNode.index].nodeDepth =  self.nodes[parentNode.index].nodeDepth +1 
            
    def ReturnTreeDepth(self):
         return max(self.nodes[node].nodeDepth for node in self.nodes)
                
    def PrintAllNodes(self):
        for node in self.nodes:
            print(self.nodes[node])
            
            
            
            



class Node:
    def __init__(self, parentNodeIndex, nodeIndex):
        self.parent = parentNodeIndex
        self.index  = nodeIndex
        self.leftChild  = None 
        self.rightChild = None
        self.nodeValue  = None
        self.nodeDepth  = None
        self.Magnitude  = None
        
    def __repr__(self):
        return "NodeIndex:" + str(self.index)
    
    def __str__(self):
        return  "NodeValue: " + str(self.nodeValue) + " NodeIndex: " + str(self.index) + " LeftChild: " + str(self.leftChild) + " RightChild: " + str(self.rightChild) + " Parent: " + str(self.parent)\
            + " Magnitude: " + str(self.Magnitude)
    def __hash__(self):
        return self.index
    
    
def BuildTree(treeEncoding):
    root = Node(None, 0)
    tree = Tree(root)
    
    currentIndex   = 0
    numberOfNodes  = 1
    characterIndex = 0
    while characterIndex < len(treeEncoding) -1:
       # print(treeEncoding[0:characterIndex])
        if treeEncoding[characterIndex] == "[" and treeEncoding[characterIndex+1] != "[":
            nextNodeValueFinalCharacterIndex = characterIndex+1
            while treeEncoding[nextNodeValueFinalCharacterIndex + 1] not in ["[", "]", ","]:
              nextNodeValueFinalCharacterIndex+=1  
            tree.AddNode(Node(currentIndex,numberOfNodes), tree.nodes[currentIndex], 1, int(treeEncoding[characterIndex+1: nextNodeValueFinalCharacterIndex+1]))
            numberOfNodes+=1
            characterIndex+=(nextNodeValueFinalCharacterIndex - characterIndex)
            
        elif treeEncoding[characterIndex] == "[" and treeEncoding[characterIndex+1] == "[":
            tree.AddNode(Node(currentIndex,numberOfNodes), tree.nodes[currentIndex], 1, None)
            currentIndex = numberOfNodes
            numberOfNodes+=1
            
        elif treeEncoding[characterIndex] == "," and treeEncoding[characterIndex+1] != "[":
            nextNodeValueFinalCharacterIndex = characterIndex+1
            while treeEncoding[nextNodeValueFinalCharacterIndex + 1] not in ["[", "]", ","]:
              nextNodeValueFinalCharacterIndex+=1 
            tree.AddNode(Node(currentIndex,numberOfNodes), tree.nodes[currentIndex], 0, int(treeEncoding[characterIndex+1: nextNodeValueFinalCharacterIndex+1]))
            numberOfNodes+=1
            characterIndex+= (nextNodeValueFinalCharacterIndex - characterIndex)
            
        elif treeEncoding[characterIndex] == "," and treeEncoding[characterIndex+1] == "[":
            tree.AddNode(Node(currentIndex,numberOfNodes), tree.nodes[currentIndex], 0, None)
            currentIndex = numberOfNodes
            numberOfNodes+=1
            
            
        elif treeEncoding[characterIndex] == "]":
            if currentIndex == 0:
                pass
            else:
                currentIndex = tree.nodes[currentIndex].parent
        
            
        characterIndex +=1
        
        
        
    return tree    


def CalculateTreeMagnitude(tree):
    #Add leaf magnitudes first:
    for node in tree.nodes:
        if tree.nodes[node].Magnitude == None and tree.nodes[node].nodeValue != None:
            if tree.nodes[tree.nodes[node].parent].leftChild == node:
                tree.nodes[node].Magnitude = tree.nodes[node].nodeValue
            else:
                tree.nodes[node].Magnitude = tree.nodes[node].nodeValue
                
                
     #Now repeat through the rest of the tree until everything has a value:
    counter = 0
    while True:    
         while counter not in tree.nodes: 
             counter = GetNextHighestIndex(tree, counter) 
         
         if   tree.nodes[counter].Magnitude == None and   tree.nodes[tree.nodes[counter].leftChild].Magnitude != None and\
              tree.nodes[tree.nodes[counter].rightChild].Magnitude != None :
              tree.nodes[counter].Magnitude = 3*tree.nodes[tree.nodes[counter].leftChild].Magnitude  + 2*tree.nodes[tree.nodes[counter].rightChild].Magnitude 
              counter = 0
              
              
         elif counter ==   GetMaxIndexInTree(tree):
             return tree.nodes[0].Magnitude

         else:
             counter = GetNextHighestIndex(tree, counter)
             
        
def GetFirstUpperNodeWithLeftChild(tree, index):
    upperIndex = index
    previousIndex = None
    while tree.nodes[upperIndex].parent != None and  tree.nodes[tree.nodes[upperIndex].parent].leftChild ==  upperIndex:
        previousIndex = upperIndex
        upperIndex = tree.nodes[upperIndex].parent   
    previousIndex = upperIndex    
    upperIndex = tree.nodes[upperIndex].parent
    
    if upperIndex == 0 and tree.nodes[0].leftChild ==  previousIndex:
        upperIndex = None
    
    if upperIndex == index:
        upperIndex = None
          
    return upperIndex

def GetFirstUpperNodeWithRightChild(tree, index):
    upperIndex = index
    previousIndex = None
    while tree.nodes[upperIndex].parent != None and  tree.nodes[tree.nodes[upperIndex].parent].rightChild ==  upperIndex:
        previousIndex = upperIndex
        upperIndex = tree.nodes[upperIndex].parent
    previousIndex = upperIndex    
    upperIndex = tree.nodes[upperIndex].parent
    
    if upperIndex == 0 and tree.nodes[0].rightChild ==  previousIndex:
        upperIndex = None
    
    if upperIndex == index:
        upperIndex = None
        
    return upperIndex


def ResolveOverflow(nodeIndex, tree): 
    #Now split this node:
    leftValue  = math.floor((tree.nodes[nodeIndex].nodeValue)/2)   
    rightValue = math.ceil((tree.nodes[nodeIndex].nodeValue)/2)
    
    nextHighestIndex = GetNextHighestIndex(tree, tree.nodes[nodeIndex].index)
    indexDifference = nextHighestIndex - nodeIndex
    tree.AddNode(Node(nodeIndex, nodeIndex+ (indexDifference/3)), tree.nodes[nodeIndex], 1, leftValue)
    tree.nodes[nodeIndex].leftChild = tree.nodes[nodeIndex+ (indexDifference/3)].index
    
    tree.AddNode(Node(nodeIndex,  nodeIndex+ (2*indexDifference/3)), tree.nodes[nodeIndex], 0, rightValue)
    tree.nodes[nodeIndex].rightChild = tree.nodes[nodeIndex+ (2*indexDifference/3)].index
    
    tree.nodes[nodeIndex].nodeValue = None
    
    return tree
    
    
def GetNextHighestIndex(tree, nodeIndex): 
     nextHighestIndex = 100000
     for node in tree.nodes:
         if tree.nodes[node].index > nodeIndex and tree.nodes[node].index < nextHighestIndex:
             nextHighestIndex = tree.nodes[node].index 
     return nextHighestIndex        
    
          
            
def ResolveExplosion(nodeIndex, tree):   
    #Left Side First:
    highestPathNode = GetFirstUpperNodeWithLeftChild(tree, nodeIndex)    
    
    if highestPathNode == None:
        #We do nothing
        pass
    else:
        leftExplosionNode = tree.nodes[highestPathNode].leftChild
        while tree.nodes[leftExplosionNode].rightChild != None:
            leftExplosionNode = tree.nodes[leftExplosionNode].rightChild
        #We add the left part of the exploding pair.
        valueToIncrement = tree.nodes[tree.nodes[nodeIndex].leftChild].nodeValue
        tree.nodes[leftExplosionNode].nodeValue = int(tree.nodes[leftExplosionNode].nodeValue) + int(valueToIncrement)
        #Remove left exploding node:
    del tree.nodes[tree.nodes[nodeIndex].leftChild]    
        
        
    #Now the right side:
    highestPathNode = GetFirstUpperNodeWithRightChild(tree, nodeIndex)
    if highestPathNode == None:
        #We do nothing
        pass
    else:
        rightExplosionNode = tree.nodes[highestPathNode].rightChild
        while tree.nodes[rightExplosionNode].leftChild != None:
            rightExplosionNode = tree.nodes[rightExplosionNode].leftChild
        #We add the left part of the exploding pair.
        valueToIncrement = tree.nodes[tree.nodes[nodeIndex].rightChild].nodeValue
        tree.nodes[rightExplosionNode].nodeValue = int(tree.nodes[rightExplosionNode].nodeValue) + int(valueToIncrement)
        #Remove left exploding node:
    del tree.nodes[tree.nodes[nodeIndex].rightChild] 
     
    #Finally add 0 in to the node index.
    tree.nodes[nodeIndex].nodeValue = 0
    tree.nodes[nodeIndex].leftChild = None
    tree.nodes[nodeIndex].rightChild = None
    return tree#, leftExplosionNode, rightExplosionNode    

def GetMaxIndexInTree(tree):
    maxIndex = 0
    for node in tree.nodes:
        if tree.nodes[node].index > maxIndex:
            maxIndex = tree.nodes[node].index           
    return maxIndex        
    


def ResolveTree(tree):
    counter = 0
    while True:
       # maxIndex = GetMaxIndexInTree(tree)
        while counter not in tree.nodes: 
            counter = GetNextHighestIndex(tree, counter)
        
        #Start with explosions   
        if tree.nodes[counter].nodeDepth > 4 :
            tree= ResolveExplosion(tree.nodes[counter].parent, tree)
            #print(EncodeTree(tree))
            counter = 0
        elif counter != GetMaxIndexInTree(tree):
                counter = GetNextHighestIndex(tree, counter)          
        #Move to splits
        elif counter == GetMaxIndexInTree(tree):  
            #Splits
            counter = 0
            overFlowCounter = 0
            while overFlowCounter not in tree.nodes: 
                overFlowCounter = GetNextHighestIndex(tree, overFlowCounter)
            while True:
                if tree.nodes[overFlowCounter].nodeValue != None and tree.nodes[overFlowCounter].nodeValue > 9 :
                    tree = ResolveOverflow(overFlowCounter, tree)
             #       print(EncodeTree(tree))
                    break
                
                elif overFlowCounter == GetMaxIndexInTree(tree):
                     return tree
                 
                else:
                    overFlowCounter = GetNextHighestIndex(tree, overFlowCounter)    
                
     
def EncodeTree(tree):
    outputString = "["   
    currentIndex = 0
    finishedNodes = []
    while True:
        #Move to left nodes if possible
        #print(outputString)
        if tree.nodes[currentIndex].leftChild !=None and tree.nodes[currentIndex].leftChild not in finishedNodes:
            currentIndex = tree.nodes[currentIndex].leftChild
            if outputString[-1] =="]":
                outputString += ",["
            else:
                outputString += "["
        
        #Move to right node if left covered already    
        elif  tree.nodes[currentIndex].leftChild !=None and tree.nodes[currentIndex].leftChild in finishedNodes and \
            tree.nodes[currentIndex].rightChild !=None and tree.nodes[currentIndex].rightChild not in finishedNodes:   
               currentIndex = tree.nodes[currentIndex].rightChild
               if outputString[-1] =="]":
                   outputString += ",["
               else:
                   outputString += "["
               
        #We're on a left child       
        elif  tree.nodes[currentIndex].leftChild ==None and tree.nodes[currentIndex].rightChild == None and \
            tree.nodes[tree.nodes[currentIndex].parent].leftChild == currentIndex:
               finishedNodes.append(currentIndex)
               outputString = outputString[0:-1]
               outputString += str(tree.nodes[currentIndex].nodeValue)  
               outputString += ","
               currentIndex = tree.nodes[currentIndex].parent
        
       #We're on a right child       
        elif  tree.nodes[currentIndex].leftChild ==None and tree.nodes[currentIndex].rightChild == None and \
           tree.nodes[tree.nodes[currentIndex].parent].rightChild == currentIndex: 
               finishedNodes.append(currentIndex)
               outputString = outputString[0:-1]
               if outputString[-1] != ",":
                   outputString += ","
               outputString += str(tree.nodes[currentIndex].nodeValue)  
               
               #outputString += "]"
               currentIndex = tree.nodes[currentIndex].parent
               
        #We're passing back up
        elif  tree.nodes[currentIndex].leftChild in finishedNodes and  tree.nodes[currentIndex].rightChild in finishedNodes and \
            tree.nodes[currentIndex].parent != None:
                finishedNodes.append(currentIndex)
                currentIndex = tree.nodes[currentIndex].parent
                outputString += "]"
        #Finish        
        elif    tree.nodes[currentIndex].leftChild in finishedNodes and  tree.nodes[currentIndex].rightChild in finishedNodes and \
            tree.nodes[currentIndex].parent == None:
                outputString += "]"
                break 
            
            
    return outputString;    
                 
        
def AddAndReduceListOfTrees(stringPath):
    treeRows = LoadInData(stringPath)
    runningTree = "[" + treeRows[0] + "," + treeRows[1] + "]"
    runningTree = BuildTree(runningTree)
    runningTree = ResolveTree(runningTree)
    #print(EncodeTree(runningTree))
    
    for tree in treeRows[2:]:
        runningTree = "[" + EncodeTree(runningTree) + "," + tree + "]"
        runningTree = BuildTree(runningTree)
        runningTree = ResolveTree(runningTree)
    
    print(EncodeTree(runningTree))    
    return runningTree    

def SolvePart1(stringPath):
    tree = AddAndReduceListOfTrees(stringPath)           
    return CalculateTreeMagnitude(tree)


    
def SolvePart2(stringPath): 
    treeRows = LoadInData(stringPath) 

    maxSumMagnitude = 0
    for i in range(len(treeRows)-1):
        print(i)
        for j in range(i+1, len(treeRows)):
            runningTree = "[" + treeRows[i] + "," + treeRows[j] + "]"
            runningTree = BuildTree(runningTree)
            runningTree = ResolveTree(runningTree)
            mag = CalculateTreeMagnitude(runningTree)
            if mag > maxSumMagnitude:
                maxSumMagnitude = mag
                
            runningTree = "[" + treeRows[j] + "," + treeRows[i] + "]"
            runningTree = BuildTree(runningTree)
            runningTree = ResolveTree(runningTree)
            mag = CalculateTreeMagnitude(runningTree)
            if mag > maxSumMagnitude:
                 maxSumMagnitude = mag    
    #print(maxSumMagnitude)            
    return maxSumMagnitude
                
                
print("Solution Part 1:", SolvePart1(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p18\p18.txt") )             
 
print("Solution Part 2:", SolvePart2(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p18\p18.txt") )            
        
#tree = AddAndReduceListOfTrees(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p18\p18.txt")           

#print(CalculateTreeMagnitude(tree))
            
#t = BuildTree("[[7,[8,4]],1]")            
#t = BuildTree("[[[[3,6],[3,6]],[0,2]],[[[8,3],9],[[3,4],8]]]")            
# t  = BuildTree("[[[[[9,8],1],2],3],4]")  
# t.PrintAllNodes()      
# print("----------------")   
# t2 = ResolveExplosion(3, t)       
# t2.PrintAllNodes()    
        
# t3 = BuildTree("[[[[0,7],4],[15,[0,13]]],[1,1]]")
# t3.PrintAllNodes()
# print("----------------")  
# t33 = ResolveOverflow(7, t3)
# t33.PrintAllNodes()

# t4 = BuildTree("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
# # t4.PrintAllNodes()
# # print("----------------")
# t5 = ResolveTree(t4)
# print(EncodeTree(t5))

# t5.PrintAllNodes()

#t4 = BuildTree("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
# t4 = BuildTree("[[7,[8,4]],1]")  
# t4.PrintAllNodes()
# print("----------------")
# print(RepackageTree(t4))


#t1 = BuildTree("[[[[1,1],[2,2]],[3,3]],[4,4]]")
#t2 = BuildTree("[[9,1],[1,9]]")
#print(CalculateNodeMagnitudes(t2))

        
            