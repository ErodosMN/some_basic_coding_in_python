# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:06:42 2019

@authors: Megi, Mino, Jacob
"""
import words, visual, ytmath

class youngtableau:
    
    def __init__(self,word):
        self.tableau=words.parse_word(word)    
    
    # returns string of underlying word
    def __str__(self):  # not working
        return self.word("string")
    
    def __mul__(self,other):
        return multiply(self,other)
    
    def visual(self,boxlength=1,file='file',grid="grid_off"):
        visual.print_tex(self.tableau,boxlength,file,grid)
    
    def row_insert(self,x):
       return ytmath.row_insert(self.tableau,x)
#        return self
    
    def word(self, mode = "object"):
        string=''
        for row in self.tableau:
            for char in row:
                string+=str(char)+' '
        if mode == "string" :
            return string.rstrip()
        else :
            return word(string.rstrip())

    
def create_from(row,file):
    #Erstelle ein Objekt der Klasse Youngtableau aus der Zeile einer Datei
    younglist=words.parse(row,file)
    young=youngtableau("")
    young.tableau=younglist
    return young
    
def multiply(T1,T2):
        
    prod=ytmath.mult_young(T1.tableau,T2.tableau)
    young=youngtableau("")
    young.tableau=prod
    return young
    
"""
#################################################################
"""


class word:
    
    def __init__(self,word):
        self.char=word.split(' ')
        self.int=[]
        if word != "" :
            for l in self.char:
                try: 
                    self.int.append(int(l))
                except:
                    raise ValueError("Kein gültiges Wort")
                    
    def __str__(self):
        W = ""
        for elem in self.int :
            W += "{} ".format(elem)
        return W.rstrip()
        
    def __mul__(self,other):
        return mult_classes(self,other)
    
    #Implementierung von K1, K1inv, K2, K2inv        
    def K1(self,index):
        #Implementierung von K1
        L,y,z,x,S=self.int,index,index+1,index+2,self.char
        if len(L)>=index+2 and L[x]<L[y] and L[y]<=L[z]:
                L[z],L[x]=L[x],L[z]
                S[z],S[x]=S[x],S[z]

        else:
            raise ValueError('K-operation impossible')
    
    def K1_inv(self,index):
        L,y,x,z,S=self.int,index,index+1,index+2,self.char
        if len(L)>=index+2 and L[x]<L[y] and L[y]<=L[z]:
                L[z],L[x]=L[x],L[z]
                S[z],S[x]=S[x],S[z]
                
        else:
            raise ValueError('K-operation impossible')
    
    def K2(self,index):
        L,x,z,y,S=self.int,index,index+1,index+2,self.char
        if len(L)>=index+2 and L[x]<=L[y] and L[y]<L[z]:
                L[z],L[x]=L[x],L[z]
                S[z],S[x]=S[x],S[z]
                
        else:
            raise ValueError('K-operation impossible')
            
    def K2_inv(self,index):
        L,z,x,y,S=self.int,index,index+1,index+2,self.char
        if len(L)>=index+2 and L[x]<=L[y] and L[y]<L[z]:
                L[z],L[x]=L[x],L[z]
                S[z],S[x]=S[x],S[z]
                
        else:
            raise ValueError('K-operation impossible')
            
    def youngtableau(self):
        young=youngtableau(self.char[0])
        #print(young.tableau)
        for intg in self.int[1:]:
            #print(intg,'000000')
            young.row_insert(intg)
            #print(young.tableau)
        
        return young
    

def mult_classes(word1,word2):
    """
    Ein Repräsentant der Äquivalenzklasse word1*word2 wird zurückgegeben.
    Für eine Eindeutige Rückgabe, wird das Wort zurükgegeben, das ein YoungTableaux darstellt.
    """
    product=ytmath.mult_young(word1.youngtableau().tableau,word2.youngtableau().tableau)
        
    string=''
    for row in product:
        for el in row:
            string+=str(el)+' '
    
    return word(string[:-1])
        
    
def are_equiv(word1,word2):
    """
    Zwei Wörter sind äquivalent, falls sie dasselbe youngtableau erzeugen.
    
    """
    return word1.youngtableau().tableau == word2.youngtableau().tableau








