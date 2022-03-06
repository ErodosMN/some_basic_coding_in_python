# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:41:31 2019

@author: Jacob
"""

import random

class Node : # (key, leftChild, rightChild)
    def __init__ (self, key=-1, leftChild=None, rightChild=None) :
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
 
 
def heights (initlist, t) :
    
    rootslist = []
    
    for i,edge in enumerate(initlist[:t]):
    
        pos1 = -1
        pos2 = -1
        
        for j in range(len(rootslist)):
            rootleaves = rootslist[j].leaves()
#            print ("leaveslist = "+str(rootleaves), j)
            if edge[0] in rootleaves: # IndexError in some cases of test2
                pos1 = j
            if edge[1] in rootleaves:
                pos2 = j
        
        
        if pos1 != pos2 :
            if pos1 != -1 and pos2 != -1:
                if min(rootslist[pos1].leaves()) < min(rootslist[pos2].leaves()):
                    nodei = Node (-1, rootslist[pos1], rootslist[pos2])
                else :
                    nodei = Node (-1, rootslist[pos2], rootslist[pos1])
                unwanted = [rootslist[pos1],rootslist[pos2]]
                rootslist = [e for e in rootslist if e not in unwanted]
            elif pos1 != -1:
                newChild = Node (initlist[i][1], None, None)
                if min(rootslist[pos1].leaves()) < initlist[i][1] :
                    nodei = Node (-1, rootslist[pos1], newChild)
                else:
                    nodei = Node (-1, newChild, rootslist[pos1])
                rootslist.pop(pos1)
            elif pos2 != -1:
                newChild = Node (initlist[i][0], None, None)
                if min(rootslist[pos2].leaves()) < initlist[i][0] :
                    nodei = Node (-1, rootslist[pos2], newChild)
                else:
                    nodei = Node (-1, newChild, rootslist[pos2])
                rootslist.pop(pos2)
                
            rootslist.append(nodei)
            
        elif pos1 == -1 and pos2 == -1 :
            lChild = Node (min(edge), None, None)
            rChild = Node (max(edge), None, None)
            nodei = Node (-1, lChild, rChild)
            rootslist.append(nodei)
    
#    id_by_leaves = []
#    for root in rootslist:
#        id_by_leaves.append(root.leaves())
#    print ("roots(idbyL) = "+str(id_by_leaves))
    
    
    heightlist = []
    for root in rootslist:
        heightlist.append(root.height())
    
    return sorted(heightlist)


def test1():
    initlist = [(2,3),(1,0),(2,4),(3,4),(3,0)]
    
    print (heights(initlist,0) == [], heights(initlist,0))
    print (heights(initlist,1) == [1], heights(initlist,1))
    print (heights(initlist,2) == [1,1], heights(initlist,2))
    print (heights(initlist,3) == [1,2], heights(initlist,3))
    print (heights(initlist,4) == [1,2], heights(initlist,4))
    print (heights(initlist,5) == [3], heights(initlist,5))
    
def test2(n):
    L = []
    for j in range (n):
        a = random.randint(0,n)
        b = random.randint(0,n)
        if a != b :
            L.append((a,b))
#    print (L)
    for i in range (n):
        heights(L,i)
    if n//2 != 0 :
        return test2(n//2)
    else:
        return 1
    
# [(3, 4), (0, 3), (5, 2), (0, 4), (4, 3)] - falsche ausgaben für diese spezielle liste
