# -*- coding: utf-8 -*-
"""
Created on Fri May  3 23:06:58 2019

@author: Jacob
"""
import random
"""

es soll tiefensuche impementiert werden
der graph muss nicht zusammenhängend sein
keine knoten übergeben, also n = 0 -> return []
keine topologische sortierung -> return [-1]

book entry (carmen):
    1. call dfs(G) to compute finishing times v.f for each vertex v
    2. as each vertex is finished insert it into the front of a linked list
    3. return the linked list of vertices

"""

class Node :
    def __init__ (self, successors, name, color = "white"):
        self.successors = successors
        self.name = name
        self.color = color

    # main function
def top_order(graph): # eingabe: liste von elem der classe Node
    global L,cycle
    cycle = 0
    L = []
    for node in graph:
        if node.color == "white":
            visit(node)
    for x in L : # ein zweiter check in visit - nach dem rekursiven aufruf, würde diese schleife ersetzen
        if x == -1 : 
            return [-1]
    return L # [node.name for node in L]

    # dfs recursion
def visit(node):
    global L,cycle
    if cycle == 1 or node.color == "black" : 
        return
    if node.color == "gray" : 
        L = [-1] # append würde (noch) schlechter funktionieren
        cycle = 1
        return 
    node.color = "gray"
    for succ in node.successors:
        visit(succ)
    node.color = "black"
    L.insert(0,node.name) # schlechte Laufzeit, besser mit einer klasse doppelt verlinkter elemente
        
    


def simple_test(n):
    graph = []
    for i in range(n):
        graph.append(Node([],i,"white"))
    for j,node in enumerate(graph):
        if j != n-1:
            node.successors = [graph[j+1]]
    print ([(node.name, [succ.name for succ in node.successors]) for node in graph])
    return top_order(graph)

def random_test(n):
    
    graph = [Node([],i,"white") for i in range(n)]
    
    foo = []
    for i in range(n):
        m = random.randint(0,n-1)
        if m not in foo :
            foo.append(m)
    
    for k,l in enumerate(foo):
        if k != l :
            (graph[k].successors).append(graph[l])
            
    print ([(node.name, [succ.name for succ in node.successors]) for node in graph])
    
    return top_order(graph)

""" top_sort from wikipedia: topological sorting
    L ← Empty list that will contain the sorted nodes
while exists nodes without a permanent mark do
    select an unmarked node n
    visit(n)

function visit(node n)
    if n has a permanent mark then return
    if n has a temporary mark then stop   (not a DAG)
    mark n with a temporary mark
    for each node m with an edge from n to m do
        visit(m)
    remove temporary mark from n
    mark n with a permanent mark
    add n to head of L
"""
""" dfs from cormen et. al.
def deep_field_search(graph):
#    for node in graph:
#        node.color = "white"
#        node.phi = 0
    global time
    time = 0
    for node in graph:
        if node.color == "white":
            dfs_visit(graph,node)
            
def dfs_visit(graph,node):
    time = time + 1
    node.discovery = time
    node.color = "gray"
    for succ in node.successors:
        if node.color == "white":
            node.phi = succ
            dfs_visit(graph,succ)
    node.color = "black"
    time = time + 1
    node.finish = time
"""