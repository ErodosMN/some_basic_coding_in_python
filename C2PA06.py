import math

# from items_class import Node, Items

from collections import deque

class Node:
    
    def __init__(self, key, freq, name, l = None, r = None):
        self.key = key             #
        self.freq = freq 
        self.name = name           # 
        self.left = l              # left child
        self.right = r             # right child

    # an order function so that the Nodes can be ordered by priority
    def __lt__(self, other):
        return self.key < other.key

    # the name of the node
    def __str__(self):
        return str(self.name)

class Items():
    
    def __init__(self, itemstring):
        self.itemlist = list(map(lambda st: (int(st.split()[0]),int(st.split()[1]),st.split()[2]),itemstring.split(',')))
        

    def __traverse(self, startnode):
        qu = deque([])
        tree_list = []
        qu.append(startnode)
        while qu:
            cur = qu.popleft()
            nodestr = [str(cur)]            
            if cur.left != None:
                qu.append(cur.left)
                nodestr.append(str(cur.left))
            else:
                nodestr.append('*')
            if cur.right != None:
                qu.append(cur.right)
                nodestr.append(str(cur.right))
            else:
                nodestr.append('*')
            tree_list.append(' '.join(nodestr))
        return tree_list


    def __str__(self):
        try:
            tree_list = self.__traverse(self.getRoot())
            return ' '.join(str(node) for node in tree_list)
        except AttributeError:
            return ' '.join([str(nn) for nn in self.itemlist])

def create (self):
        
        n = len(self.nodelist)

        costs_list = [[node.freq] for node in self.nodelist]
        roots_list = [[i] for i in range (len(self.nodelist))]
        print (costs_list)
        print (roots_list)
        
        for k in range (len(costs_list)):
            for i in range (len(costs_list) - k):
                j = i + k
                print (k,i,j)
#                co_l = []
                
                
                minimum = math.inf
                m = 0
                for l in range (i,j+1):
                    if l == i :
                        x = 0
                    else :
                        x = costs_list[i][l-1]
                    if l == j+1 :
                        y = 0
                    else :
                        y = costs_list[l+1][i]
                    
                    if x + y < minimum :
                        minimum = x + y
                        m = l-i
#                    co_l.append(x+y)
                
                q = 0
                for a in range (i,j+1):
                    q += costs_list[a][0]
                
                costs_list[i].append(q + minimum)
                roots_list[i].append(m)
        
                        
        print (m)
        print (costs_list)
        print (roots_list)
        return 1,1

def buildTree(self, n, roots_list):
        
        return "ff"


class StaticSearchTree (Items) : 
    def __init__ (self, itemstring) : # init with list of triplets (key,freq,name)
        super().__init__(itemstring)
        self.itemlist.sort()
        self.nodelist = [Node(key,freq,name) for (key,freq,name) in self.itemlist]
        
        self.root , self.costs = create(self)
        
        

    def getMin(self,node_x,node_y):
        
        if node_x.freq == node_y.freq :
            return min(node_x.key, node_y.key)
        else :
            if node_x.freq < node_y.freq :
                return node_x
            else :
                return node_y
        
    
    def minCost(self):
        return self.costs
                
                
#                cur = "placeholder", d = 1):
#        
#        if cur == "placeholder" :
#            cur = self.getRoot()
#        
#        if cur == None :
#            return 0
#        
#        costs = cur.freq * d
#        
#        costs += self.minCost(cur.left, d+1)
#        costs += self.minCost(cur.right, d+1)
#        
#        return costs
#    
#    
    def getRoot(self):
        return self.root
                



def test():
#    \textsc {s = StaticSearchTree ('27 85 Node1 ,30 42 Node2 , \
#    4 23 Node3 ,24 70 Node4 ,2 15 Node5 ,5 71 Node6')}
    
    s = StaticSearchTree ('27 85 Node1 ,30 42 Node2 ,4 23 Node3 ,24 70 Node4 ,2 15 Node5 ,5 71 Node6')
    
    print (s. getRoot () == "Node4")
    print (s.minCost() == 637)












