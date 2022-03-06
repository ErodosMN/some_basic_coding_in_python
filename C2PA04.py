# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:09:58 2019

@author: Jacob
"""
    # naive implementierung der zugrundeliegenden klasse
class Set :
    def __init__ (self, representative, value) :
        self.rep = representative
        self.values = [value]
        
    def Elements (self) :
        return sorted(self.values)
    
    def __str__ (self) :
        return self.Elements()
    
    
class Partition (Set) :
    def __init__ (self, input_list):
        self.Sets = [Set(n,n) for n in input_list]
    
    def MakeSet (self, intager):
        for i,s in enumerate (self.Sets):
            if intager == s.rep or intager in s.values :
                raise Exception ("invalid operation")
        self.Sets.append(Set(intager,intager))
    
    def FindSet (self, intager):
        for s in self.Sets:
            if intager in s.values :
                return s.rep
        raise Exception ("invalid operation")
    
    def Union (self, val_x, val_y) : # add values of x to y and then delete x from self.Sets
         rep_x = self.FindSet(val_x)
         rep_y = self.FindSet(val_y)
         
         if rep_x == rep_y : return
         
         Set_x = -1
         Set_y = -1
         for s in self.Sets:
            if rep_x == s.rep :
                Set_x = s
            if rep_y == s.rep :
                Set_y = s
                
         if len(Set_x.values) < len(Set_y.values) :
             Set_y.values.extend(Set_x.values)
             self.Sets.remove(Set_x)
         else :
             Set_x.values.extend(Set_y.values)
             self.Sets.remove(Set_y)



def test (given_list = [1,2,3]) :
    p = Partition (given_list)
    
    p.MakeSet(4)
    p.Union(3,4)
    p.Union(1,3)
    
    print(p.Sets[0].Elements())
    print (p.Sets[1].Elements())
    
    print (p.FindSet(4))










