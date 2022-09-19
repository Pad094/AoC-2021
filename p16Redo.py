# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 23:03:58 2021

@author: Padraig
"""

p1Test = "220D6448300428021F9EFE668D3F5FD6025165C00C602FC980B45002A40400B402548808A310028400C001B5CC00B10029C0096011C0003C55003C0028270025400C1002E4F19099F7600142C801098CD0761290021B19627C1D3007E33C4A8A640143CE85CB9D49144C134927100823275CC28D9C01234BD21F8144A6F90D1B2804F39B972B13D9D60939384FE29BA3B8803535E8DF04F33BC4AFCAFC9E4EE32600C4E2F4896CE079802D4012148DF5ACB9C8DF5ACB9CD821007874014B4ECE1A8FEF9D1BCC72A293A0E801C7C9CA36A5A9D6396F8FCC52D18E91E77DD9EB16649AA9EC9DA4F4600ACE7F90DFA30BA160066A200FC448EB05C401B8291F22A2002051D247856600949C3C73A009C8F0CA7FBCCF77F88B0000B905A3C1802B3F7990E8029375AC7DDE2DCA20C2C1004E4BE9F392D0E90073D31634C0090667FF8D9E667FF8D9F0C01693F8FE8024000844688FF0900010D8EB0923A9802903F80357100663DC2987C0008744F8B5138803739EB67223C00E4CC74BA46B0AD42C001DE8392C0B0DE4E8F660095006AA200EC198671A00010E87F08E184FCD7840289C1995749197295AC265B2BFC76811381880193C8EE36C324F95CA69C26D92364B66779D63EA071008C360098002191A637C7310062224108C3263A600A49334C19100A1A000864728BF0980010E8571EE188803D19A294477008A595A53BC841526BE313D6F88CE7E16A7AC60401A9E80273728D2CC53728D2CCD2AA2600A466A007CE680E5E79EFEB07360041A6B20D0F4C021982C966D9810993B9E9F3B1C7970C00B9577300526F52FCAB3DF87EC01296AFBC1F3BC9A6200109309240156CC41B38015796EABCB7540804B7C00B926BD6AC36B1338C4717E7D7A76378C85D8043F947C966593FD2BBBCB27710E57FDF6A686E00EC229B4C9247300528029393EC3BAA32C9F61DD51925AD9AB2B001F72B2EE464C0139580D680232FA129668"

testString = "110100101111111000101000"
test2      = "11101110000000001101010000001100100000100011000001100000"
test3 = "11010001010"
test4 = "0101001000100100"
test5 = "D2FE28"

def hexToBinaryStringConvertor(string):
    converterDictionary = {}
    converterDictionary["0"] = "0000"
    converterDictionary["1"] = "0001"
    converterDictionary["2"] = "0010"
    converterDictionary["3"] = "0011"
    converterDictionary["4"] = "0100"
    converterDictionary["5"] = "0101"
    converterDictionary["6"] = "0110"
    converterDictionary["7"] = "0111"
    converterDictionary["8"] = "1000"
    converterDictionary["9"] = "1001"
    converterDictionary["A"] = "1010"
    converterDictionary["B"] = "1011"
    converterDictionary["C"] = "1100"
    converterDictionary["D"] = "1101"
    converterDictionary["E"] = "1110"
    converterDictionary["F"] = "1111"
    
    convertedString = ""
    for character in string:
        convertedString += converterDictionary[character]
    
    return convertedString     

def PreenLiteralString(string):
    newString = string[0:6]
    nextStartIndex =6
    while int(string[nextStartIndex]) == 1:
        newString += string[nextStartIndex: nextStartIndex+5]
        nextStartIndex+=5
    newString+= string[nextStartIndex: nextStartIndex+5]
    
    return newString


def GetLiteralVersionNumber(string):
    versionNumber = string[0:3]
    decimalValue = 0
    for i in range(3):
       decimalValue += 2**(2-i)*int(versionNumber[i])
    return decimalValue   


def ReturnMessageTypeID(string):
    typeID = string[3:6]
    decimalValue = 0
    for i in range(3):
       decimalValue += 2**(2-i)*int(typeID[i])
    return decimalValue 


def GetOperatorID(string):
    return int(string[6])
    


def GetOperatorID0Length(string):
    operatorID0Length = 0
    lengthChunck       = string[7: 22]
    
    for i in range(15):
        operatorID0Length+= 2**(14-i)*int(lengthChunck[i])
        
    return operatorID0Length    


def GetOperatorID1NumberOfPackets(string):
    operatorID1NumberOfPackets = 0
    lengthChunck       = string[7: 18]
    
    for i in range(11):
        operatorID1NumberOfPackets+= 2**(10-i)*int(lengthChunck[i])
        
    return operatorID1NumberOfPackets 
    



def BuildListOfAllPacketString(inputString):
    fullLength = len(inputString)
    listOfPacketStrings=[]
    
    stringIndex =0
    while stringIndex < fullLength-3 and "1" in inputString[stringIndex:]:
        #Process next string:
            #print(listOfPacketStrings)
            #print(stringIndex)
            nextStringType = ReturnMessageTypeID(inputString[stringIndex:])
            if nextStringType ==4:
                nextLiteralString = PreenLiteralString(inputString[stringIndex:])
                listOfPacketStrings.append(nextLiteralString)
                stringIndex+= len(nextLiteralString)
            
            elif GetOperatorID(inputString[stringIndex:]) == 0:
                nextOp0String = inputString[stringIndex:stringIndex+22]
                listOfPacketStrings.append(nextOp0String)
                stringIndex+= len(nextOp0String)
                
            elif GetOperatorID(inputString[stringIndex:]) == 1:
                nextOp1String = inputString[stringIndex:stringIndex+18]
                listOfPacketStrings.append(nextOp1String)
                stringIndex+= len(nextOp1String)     
                
            else:
                raise ValueError('Input that it cannot handle from index {0} ', stringIndex)
                
    return listOfPacketStrings     

      
  
t1 = "8A004A801A8002F478"
t3 =  "C0015000016115A2E0802F182340" 
t4 = "A0016C880162017C3686B18A3D4780"  
#print(hexToBinaryStringConvertor(t3))                  
#print(BuildListOfAllPacketString(hexToBinaryStringConvertor(t4)))

def SumAllVersionNumbers(string):
           packets = BuildListOfAllPacketString(hexToBinaryStringConvertor(string))
           versionSum = 0
           for packet in packets:
               versionSum += GetLiteralVersionNumber(packet)
           return versionSum
       
print("Solution Part 1:", SumAllVersionNumbers(p1Test))   




testIndicatorFunPack = "001010100000000001"
testIndicatorFunPackets = ["1010100000000000001011", "11010001111000"] 
testIsReoslvedArray = [1,1]
subpacketIndexArray = [[3],[]]



def FindLastLiteralIndexInDescendingCharin(startIndex, sliceStartIndex, subpacketIndexArray):
    
    finalSubpacketIndex = subpacketIndexArray[startIndex][-1]
    
    while subpacketIndexArray[finalSubpacketIndex - sliceStartIndex] != []:
        finalSubpacketIndex = subpacketIndexArray[finalSubpacketIndex - sliceStartIndex][-1]
        
    return finalSubpacketIndex    
    

def AddSubpacketIndicesForIndexI(packetIndex, subpacketsArray, resolutionArray, subpacketIndexArray):
    
    ##INDEX 151 BEING PROCESSED INCORRECTLY HERE
    
    packet = subpacketsArray[packetIndex]
    subpacketsToAddToIndex = [] 
    
    if GetOperatorID(packet) ==0:
        lengthToConsider = GetOperatorID0Length(packet)
        associatedPackets = []
        i = packetIndex + 1
        while sum(len(x) for x in associatedPackets) < lengthToConsider:
            associatedPackets.append(subpacketsArray[i])
            i+=1
        indicesToConsider = []
        for i in range(packetIndex + 1, packetIndex + 1 + len(associatedPackets)):
            indicesToConsider.append(i)
        indicesToRuleOut =[]
        for i in range(packetIndex + 1, packetIndex + 1 + len(associatedPackets)):
            for j in subpacketIndexArray[i]:
                if j in indicesToConsider:
                    indicesToRuleOut.append(j)
        finalIndicesToAdd = []
        for i in range(packetIndex + 1, packetIndex + 1 + len(associatedPackets)):  
            if i not in  indicesToRuleOut:
                finalIndicesToAdd.append(i)
        subpacketsToAddToIndex = finalIndicesToAdd    
        
    elif GetOperatorID(packet) == 1:
         packetNumberToConsider = GetOperatorID1NumberOfPackets(packet)
         
         
         i = packetIndex + 1
         numberOfPacketsCovered = 0
        
         while numberOfPacketsCovered < packetNumberToConsider:
                if ReturnMessageTypeID(subpacketsArray[i]) == 4:
                    numberOfPacketsCovered+=1
                    subpacketsToAddToIndex.append(i)
                    i+=1
                   
                    
                elif GetOperatorID(subpacketsArray[i]) == 0 :
                    #It's resolved so use indices to move to next valid subpacket:
                        subpacketsToAddToIndex.append(i)
                        associatedPackets = []
                        j=i+1
                        while sum(len(x) for x in associatedPackets) < GetOperatorID0Length(subpacketsArray[i]):
                            associatedPackets.append(subpacketsArray[j])
                            j+=1
                        i=j 
                        numberOfPacketsCovered+=1
                        
                elif GetOperatorID(subpacketsArray[i]) == 1:
                    subpacketsToAddToIndex.append(i)
                    #ERROR TO FIX. NUMBER OF SUBPACKETS IS NOT NEXT NUMBER OF PACKETS TO SKIP
                    #BUT WE HAVE INDEX OF FINAL SUBPACKET
                    #FIXED NOW
                    #i+= GetOperatorID1NumberOfPackets(subpacketsArray[i])
                    i = FindLastLiteralIndexInDescendingCharin(i, 0, subpacketIndexArray) +1
                    numberOfPacketsCovered+=1
                    #It's resolved so use indices to move to next valid subpacket:
                         
                else:
                    raise ValueError('Input that it cannot handle from index {0} ', i)
    subpacketIndexArray[packetIndex] =  subpacketsToAddToIndex
    return subpacketIndexArray            
         
            
        
        
        

def CanHaveSubPacketIndicesAdded(packet, packetIndex, packetStrings, isResolvedIndicatorArray, subpacketIndexArray):
    
    if GetOperatorID(packet) ==0:
        lengthToConsider = GetOperatorID0Length(packet)
        associatedPackets = []
        i = 0
        while sum(len(x) for x in associatedPackets) < lengthToConsider:
            #print(lengthToConsider, sum(len(x) for x in associatedPackets))
            associatedPackets.append(packetStrings[i])
            i+=1
        unfinishedCount = 0
        for pack in range(len(associatedPackets)):
            if isResolvedIndicatorArray[pack] !=1:
                unfinishedCount =1
                break
        if unfinishedCount == 1:
            return False
        else:
            return True
        
        
    elif GetOperatorID(packet) == 1:   
        packetNumberToConsider = GetOperatorID1NumberOfPackets(packet)
        
        
        i=0
        pack = packetStrings[i]
        numberOfPacketsCovered = 0
        
        while numberOfPacketsCovered < packetNumberToConsider:
                if ReturnMessageTypeID(packetStrings[i]) == 4:
                    numberOfPacketsCovered+=1
                    i+=1
                elif GetOperatorID(packetStrings[i]) == 0 and isResolvedIndicatorArray[i]==1: 
                    #It's resolved so use indices to move to next valid subpacket:
                        associatedPackets = []
                        j=i+1
                        while sum(len(x) for x in associatedPackets) < GetOperatorID0Length(packetStrings[i]):
                            associatedPackets.append(packetStrings[j])
                            j+=1
                        i=j 
                        numberOfPacketsCovered+=1
                        
                elif GetOperatorID(packetStrings[i]) == 1 and isResolvedIndicatorArray[i]==1: 
                    #ERROR THIS NEED TO  PASS TO MAX INDEX IN SUBPACKET ARRAY
                    
                    #i+= (2 + subpacketIndexArray[i][-1] - subpacketIndexArray[i][0]) 
                    #i+= GetOperatorID1NumberOfPackets(packetStrings[i])
                    i+= (2 + FindLastLiteralIndexInDescendingCharin(i, (packetIndex+1), subpacketIndexArray)- subpacketIndexArray[i][0])
                    numberOfPacketsCovered+=1
                    #It's resolved so use indices to move to next valid subpacket:
                elif GetOperatorID(packetStrings[i]) == 0 and isResolvedIndicatorArray[i]==0: 
                    return False
                elif GetOperatorID(packetStrings[i]) == 1 and isResolvedIndicatorArray[i]==0:       
                    return False         
                else:
                    raise ValueError('Input that it cannot handle from index {0} ', i)
       
        return True            
        
# if(CanHaveSubPacketIndicesAdded(testIndicatorFunPack, testIndicatorFunPackets, testIsReoslvedArray, subpacketIndexArray))     :
#     print("true")




def BuildSubPacketIndexArray(packetStrings):
    subpacketIndexArray      = [[] for sting in packetStrings]
    isResolvedIndicatorArray =  [0 for string in packetStrings]
    
    for i in range(len(packetStrings)):
        if ReturnMessageTypeID(packetStrings[i]) == 4:
            isResolvedIndicatorArray[i] =1
            
    while sum(isResolvedIndicatorArray) < len(isResolvedIndicatorArray):
        i = 0
        packet                             = packetStrings[i]
        successiveSubpackets               = packetStrings[i+1:].copy()
        successiveResolutionArray          = isResolvedIndicatorArray[i+1:].copy()
        successiveIndexSubpacketIndexArray = subpacketIndexArray[i+1:].copy()
        
        while ReturnMessageTypeID(packet) == 4 or\
              isResolvedIndicatorArray[i] or\
            not CanHaveSubPacketIndicesAdded(packet, i,  successiveSubpackets, successiveResolutionArray, successiveIndexSubpacketIndexArray):
            
                i+=1
                packet                             = packetStrings[i]
                successiveSubpackets               = packetStrings[i+1:].copy()
                successiveResolutionArray          = isResolvedIndicatorArray[i+1:].copy()
                successiveIndexSubpacketIndexArray = subpacketIndexArray[i+1:].copy()
        #Otherwise we've found another packet we can resolve:    
        isResolvedIndicatorArray[i] = 1
        subpacketIndexArray = AddSubpacketIndicesForIndexI(i, packetStrings, isResolvedIndicatorArray, subpacketIndexArray)
        
    return subpacketIndexArray
            
     
           
packets = BuildListOfAllPacketString(hexToBinaryStringConvertor(p1Test))
#print(packets)

#print(BuildSubPacketIndexArray(packets))


def TestPacketOutput(packets):
    numberOfPackets = len(packets)
    packetIndices = BuildSubPacketIndexArray(packets)
    packetIndicesSet = set([])
    for i in range(numberOfPackets):
        for j in packetIndices[i]:
            packetIndicesSet.add(j)
    print(numberOfPackets, len(packetIndicesSet))        
            
#print(hexToBinaryStringConvertor(t4))            
            
#print(TestPacketOutput(packets))  

def EvaluateScoreAtPacketI(packet, subpacketIndices, evaluationArray):
    versionType = ReturnMessageTypeID(packet)
    score = 0
    
    if versionType == 0:
        for index in subpacketIndices:
            score += evaluationArray[index]
            
    elif versionType == 1:
         score = 1
         for index in subpacketIndices:
             score*= evaluationArray[index]
             
    elif versionType == 2:
        score = min(evaluationArray[x] for x in subpacketIndices)

    elif versionType == 3:
        score = max(evaluationArray[x] for x in subpacketIndices)

    elif versionType == 5:
        if evaluationArray[subpacketIndices[0]] >  evaluationArray[subpacketIndices[1]]:
            score = 1
        else:
            score = 0
       
    elif versionType == 6:
        if evaluationArray[subpacketIndices[0]] <  evaluationArray[subpacketIndices[1]]:
            score = 1
        else:
            score = 0   
            
    elif versionType == 7:
        if evaluationArray[subpacketIndices[0]] ==  evaluationArray[subpacketIndices[1]]:
            score = 1
        else:
            score = 0 
        
             
    return score

def GetLiteralStringScore(packet):
    stringToDecode = packet[6:]
    decodedString  = ""
    
    for i in range(int(len(stringToDecode)/5)):
        decodedString += stringToDecode[5*i +1: 5*(i+1)]
    
    trueValue = 0   
    for i in range(len(decodedString)):
        trueValue += int(decodedString[i])*2**(len(decodedString) - i - 1)
        
    return trueValue    
        

def EvaluatePacketValues(packets):
    subpacketIndexArray      = BuildSubPacketIndexArray(packets)
    evaluationArray          = [0 for packet in packets]
    evaluationIndicatorArray = [0 for packet in packets]
    
    #First evaluation literal Strings:
    for i  in range(len(packets)):
        if subpacketIndexArray[i] == []:
            evaluationArray[i]          = GetLiteralStringScore(packets[i])
            evaluationIndicatorArray[i] = 1
            
    #Now evaluate everything else:
    while sum(evaluationIndicatorArray) < len(evaluationIndicatorArray):
        i = 0
        while evaluationIndicatorArray[i] == 1  or\
              sum(evaluationIndicatorArray[x] for x in subpacketIndexArray[i]) < len(subpacketIndexArray[i]):
                  i+=1
        #print(i)          
        evaluationIndicatorArray[i] = 1
        evaluationArray[i] = EvaluateScoreAtPacketI(packets[i], subpacketIndexArray[i], evaluationArray) 
        
    return evaluationArray    
  

s1 = "C200B40A82"
s4 = "CE00C43D881120"      
  
#print(BuildListOfAllPacketString(hexToBinaryStringConvertor(s4)))      
print("Solution Part 2:", EvaluatePacketValues(BuildListOfAllPacketString(hexToBinaryStringConvertor(p1Test)))[0])                  
                  
