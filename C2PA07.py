# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:15:28 2019

@author: Jacob
"""
# fubar
import random

class ngonTriang :
    def __init__ (self, n, triangles, test = 0) : # with n = number of corners, triangles = list of triangles
        self.t = test
        self.n = n
        
        f = len(triangles)
        
        if n < 4 or len(triangles) != n - 2 :
            raise ValueError ("no triangulation")
        
        for t in triangles :
            t.sort()
        triangles.sort()
        
        if test == 1 :
            print ("init with {},{}".format(n,triangles))
        
        self.triangles = triangles # [sorted(triple) for triple in triangles]
        
        w = []
        for i in range(f - 1):
            i0 = triangles[i][0]
            i1 = triangles[i][1]
            i2 = triangles[i][2]
            for j in range (i + 1, f):
                
                tri_j = triangles[j]
                
                if triangles[i] == tri_j :
                    raise ValueError ("no triangulation")
                
                if i0 in tri_j and i1 in tri_j :
                    w.append([i0,i1])
                if i1 in tri_j and i2 in tri_j :
                    w.append([i1,i2])
                if i0 in tri_j and i2 in tri_j :
                    w.append([i0,i2])
                    
        if test == 1 :
            print ("walls created are {}".format(w))
        
        k = len(w)
        if k != f -1 :
            raise ValueError ("no triangulation")
        for i in range (k - 1) : # i believe this to be the only actually necessary test
            i0 = w[i][0]
            i1 = w[i][1]
            for j in range (i + 1, k) :
                j0 = w[j][0]
                j1 = w[j][1]
                
                if (i0 < j0 < i1) and ((j1 < i0) or (j1 > i1)) :
                    raise ValueError ("no triangulation")
                if (i0 < j1 < i1) and ((j0 < i0) or (j0 > i1)) :
                    raise ValueError ("no triangulation")
        
        
        self.walls = sorted(w)

    def n_walls (self) :
        return len(self.walls)
    
    def flip (self, wall) :
        
        triangles = self.triangles
        n = self.n
        
        # triangles that share the wall
        tri_1 = -1
        tri_2 = -1
        
#        # positions of tri_1/2 in list of triangles
#        t_1 = -1
#        t_2 = -1
        
        # count for ... 
        k = 0
        # ... loop through list of triangles
        while tri_1 == -1 :
            if k > len(triangles)-1 : raise Exception ("false input or logic error found in first loop")
            
            if wall[0] in triangles[k] and wall[1] in triangles[k] :
                tri_1 = triangles[k]
            k += 1
        
        while tri_2 == -1 :
            if k > len(triangles)-1 : raise Exception ("false input or logic error found in second loop")
            
            if wall[0] in triangles[k] and wall[1] in triangles[k]:
                tri_2 = triangles[k]
            k += 1
        if self.t == 1 :
            print ("flip at wall: {} with 1: {} 2: {}".format(wall,tri_1,tri_2))
        # creation of new triangles
        a = [x for x in tri_1 if x not in wall]
        b = [x for x in tri_2 if x not in wall]
        new_tri_1, new_tri_2 = [wall[0]], [wall[1]]
        new_tri_1.extend(a)
        new_tri_1.extend(b)
        new_tri_2.extend(a)
        new_tri_2.extend(b)
        
        # creation of new list of triangles
        new_triangles = [elem for elem in triangles if elem not in [tri_1,tri_2]]
        new_triangles.extend([new_tri_1,new_tri_2])
        
        return ngonTriang(n,new_triangles, self.t) # fippend state as ngonTriag object


def test():
    
    T = ngonTriang(4,[[0,1,2],[0,2,3]])
    
    print(T.triangles)
    print(T.walls)
    print(T.n_walls())
    
    S = T.flip([0,2])
    
    print(S.triangles)
    
    W = ngonTriang(4,[[0,1,2],[0,2,3],[1,2,3]])
    
    
    
def random_test(n):
    
    
    v = n + 1
    triangles = [[0,1,2]]
    for i in range (2,n):
        triangles.append([0,i+1,i])
    T = ngonTriang(v,triangles,1)
    for wall in T.walls:
        S = T.flip(wall)
        for x in S.walls:
            X = S.flip(x)
            for y in X.walls:
                Y = X.flip(y)
    
def case_test():
    A = ngonTriang(6,[[0,1,2],[2,3,4],[4,5,0],[0,4,2]],1)
    
    B = ngonTriang(6,[[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5]],1)
    
    S = B.flip([0,3])
"""Gegenbeispiel zur Korrektheit
B = ngonTriang(6,[[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5]],1)
init with 6,[[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5]]
walls created are [[0, 2], [0, 3], [0, 4]]

S = B.flip([0,3])
init with 6,[[0, 1, 2, 2], [0, 3, 4], [0, 4, 5], [1, 2, 2, 3]]
walls created are [[1, 2], [0, 4]]
"""
