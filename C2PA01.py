# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:08:59 2019

@author: Jacob
"""


class Node : # (key, leftChild, rightChild)
    def __init__ (self, key, leftChild, rightChild) :
        self.key = key
        self.rightChild = rightChild
        self.leftChild = leftChild
        
        
    def keys (self) :
        keysList = [self.key]
        if self.leftChild != None :
            keysList.extend(self.leftChild.keys())
        if self.rightChild != None :
            keysList.extend(self.rightChild.keys())
        return keysList
        
    def height (self) :
        if self.leftChild != None and self.rightChild != None :
            return max(self.leftChild.height()+1, self.rightChild.height()+1)
        elif self.leftChild != None :
            return self.leftChild.height()+1
        elif self.rightChild != None :
            return self.rightChild.height()+1
        else :
            return 0

    def leaves (self) :
        leavesList = []
        if self.leftChild == None and self.rightChild == None :
            leavesList.append(self.key)
        if self.leftChild != None :
            leavesList.extend(self.leftChild.leaves())
        if self.rightChild != None :
            leavesList.extend(self.rightChild.leaves())
        return leavesList


def test2():
    nodeLL = Node (7,None,None)
    nodeL = Node (5,nodeLL,None)
    nodeRL = Node (3,None,None)
    nodeR = Node (2,nodeRL,None)
    bin2 = Node (0, nodeL,nodeR)
    
    print(bin2.keys() == [0,5,7,2,3])
    print(nodeLL.height() == 0)
    print(bin2.height() == 2)
    print(bin2.leaves() == [7,3])
    print(nodeLL.leaves() == [7])


def test1():
    nodeRLR = Node (4,None,None)
    nodeRL = Node (3,None,nodeRLR)
    nodeRR = Node (7,None,None)
    nodeL = Node (5,None,None)
    nodeR = Node (2,nodeRL,nodeRR)
    bin1 = Node (1,nodeL,nodeR)
    
    print(bin1.height() == 3)
    print(nodeRL.height() == 1)
    print(bin1.keys() == [1,5,2,3,4,7])
    print(bin1.leaves() == [5,4,7])
    print(nodeR.leaves() == [4,7])

def test3():
    right2R = Node (7,None,None)
    left2L = Node (15,None,None)
    bin1R = Node (16,left2L,right2R)
    bin3 = Node (17,None,bin1R)
    print (bin3.height() == 2)
    print (bin3.keys() == [17,16,15,7])