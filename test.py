# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:37:31 2019

@author: Megi, Mino, Jacob
"""

from struc import *
from random import randint
# subprocess imported through visual

"""

std_filenames: random_yt_words, equiv_test, file

"""


    # random creation of word object
def create_W (N = 10, R = 50):
    """
    N = length of created word
    R = [0,R] range of possible integers
    """
    w = ""
    for i in range (N) :
        w += " {}".format(randint(1,R))
    return word(w.lstrip())

    # random creation of youngtableau object
def create_YT(N = 10, R = 50):
    word = create_W(N,R)
    return word.youngtableau()


    # creates z rows of yt_words in a txt file
def create_txt(z = 5, N = 10, R = 50, filename = "random_yt_words"):
    
    BASIS = ""
    
    for i in range (z):
        yt = create_YT(N,R)
        BASIS += "{}\n".format(yt) # .word("string")
    
    with open(filename+".txt","w") as file:
        file.write(BASIS)
    
    return "finished"


def rand_swap(w):
    """
    performs one random K_swap, unless it doesn't find a valid one
    handles all exceptions
    """
    
    check = 1
    stop = 0
    while check == 1 :    
        r = randint(1,4)
        index = randint(0,len(w.int)) # zulässige indize egal
        
        if r == 1 :
            try :
                w.K1(index)
                check = 0
            except :
                ValueError
                IndexError
                
        elif r == 2 :
            try :
                w.K1_inv(index)
                check = 0
            except :
                ValueError
                IndexError
            
        elif r == 3 :
            try :
                w.K2(index)
                check = 0
            except :
                ValueError
                IndexError
            
            
        elif r == 4 :
            try :
                w.K2_inv(index)
                check = 0
            except :
                ValueError
                IndexError
                
        stop += 1
        if stop == 100 :
            break

def equiv_test(N = 10,R = 50, mode = "run"):
    
    create_txt(2, N, R, "equiv_test")
    
    ytA = create_from(0,"equiv_test.txt")
    ytB = create_from(1,"equiv_test.txt")
    
    if mode == "show" :
        print ("initial tableaux:\n{}\n{}".format(ytA,ytB))
    
    wA = ytA.word()
    wB = ytB.word()
    
    word1 = (ytA * ytB).word()
    word2 = wA * wB
    
    if mode == "show" :
        print ("multiplied words:\n{}\n{}".format(word1,word2))
    
    for i in range (10):
        rand_swap(word1)
        rand_swap(word2)
        
    if mode == "show" :
        print ("randomly swapped words:\n{}\n{}".format(word1,word2))
    
    return are_equiv(word1,word2)
    









