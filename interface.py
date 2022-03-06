#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:54:06 2019

@author: mino
"""
from struc import *
from test import *
import random
import tkinter as tk

root= tk.Tk()
root.title("YoungTableaux")

canvas1 = tk.Canvas(root, width = 800, height = 500,  relief = 'raised')
canvas1.pack()

"""
LABELS
"""
title = tk.Label(root, text='Young Tableaux Tool')
title.config(font=('helvetica', 14))
label2 = tk.Label(root, text='Enter a word representing a young tableau:')
label2.config(font=('helvetica', 10))
equiv_entry_text = tk.Label(root,text="Enter two words to check for equivalency.",font=('helvetica', 10, 'bold'))
mult_text=tk.Label(root,text="Enter two words to multiply.",font=('helvetica', 10, 'bold'))
create_random_YT_text = tk.Label(root,text="Click below to create a random young tableau with maximal length 30 and numbers out of the range 1 to 100.",font=('helvetica', 10, 'bold'))
create_equiv_text = tk.Label(root,text="Enter a word and click below to randomly generate an equivalent word.",font=('helvetica', 10, 'bold'))
equiv_created1 = tk.Label(root,text="A random equivalent word is:",font=('helvetica', 10, 'bold'))
equiv_created2 = tk.Label(root,text="The unique young tableau respresentative of this equivalency class is",font=('helvetica', 10, 'bold'))
boxlength_text = tk.Label(root,text="Enter boxlength (Default = 1)",font=('helvetica', 10,))


"""
ENTRIES
"""
word1_entry = tk.Entry (root) 
word2_entry = tk.Entry (root)
entry1 = tk.Entry (root) 
entrybox = tk.Entry(root)




def base():
    canvas1.delete("all")
    canvas1.create_window(400, 25, window=title)


def random_YT_setup():
    base()
    canvas1.create_window(400, 400, window=button_reset)
    canvas1.create_window(400, 80, window=create_random_YT_text)

    canvas1.create_window(400, 140, window=button_create_random)

    
    
    
    
def create_random_YT():
    n=random.randint(1,30)
    randomYT=(" ").join(create_YT(n,100).word().char)
    label_random_YT=tk.Label(root,text=randomYT,font=('helvetica', 10, 'bold'))
    canvas1.create_window(400, 200, window=label_random_YT)
    entry1.delete(0, 'end')
    entry1.insert(0,randomYT)
    canvas1.create_window(400, 250, window=button_vis)
    
    
    
    
def random_k_setup():
    base()
    canvas1.create_window(400, 400, window=button_reset)
    canvas1.create_window(400, 80, window=create_equiv_text)
    entry1.delete(0, 'end')
    canvas1.create_window(400, 140, window=entry1)

    canvas1.create_window(400, 180, window=button_create_equiv)
    entry1.focus_set()
    
    


def create_random_equiv():
    n=random.randint(1,30)
    given_word=word(str(entry1.get()))
    for _ in range(n):
        rand_swap(given_word)
    yt_word=(" ").join(given_word.youngtableau().word().char)
    equiv_label = tk.Label(root,text=(" ").join(given_word.char),font=('helvetica', 10, 'bold'))
    equiv_yt_word = tk.Label(root,text=yt_word,font=('helvetica', 10, 'bold'))

    canvas1.create_window(400, 210, window=equiv_created1)
    canvas1.create_window(400, 240, window=equiv_label)
    canvas1.create_window(400, 270, window=equiv_created2)
    canvas1.create_window(400, 300, window=equiv_yt_word)

    entry1.delete(0, 'end')
    entry1.insert(0,yt_word)


    canvas1.create_window(400, 350, window=button_vis)

    



def check_equiv_setup():
    word1_entry.delete(0, 'end')
    word2_entry.delete(0, 'end')

    base()

    
    canvas1.create_window(400, 100, window=equiv_entry_text)
    canvas1.create_window(250, 130, window=word1_entry)
    canvas1.create_window(550, 130, window=word2_entry)
    canvas1.create_window(400, 170, window=button_equiv)
    canvas1.create_window(400, 400, window=button_reset)


    word1_entry.focus_set()


def check_equiv():
    canvas1.delete("result_equiv")
    
    word1=word(str(word1_entry.get()))
    word2=word(str(word2_entry.get()))
    
    if are_equiv(word1,word2):
        result="The given words are equivalent and therefore result in the same young tableau."
    else:
        result="The given words are not equivalent and thus represent different young tableaus."

    result_equiv=tk.Label(root,text=result,font=('helvetica', 10, 'bold'))
    canvas1.create_window(400, 250, window=result_equiv)
    
    

    





def vis_new():
    x1 = str(entry1.get())
    boxl=1
    L=entrybox.get()
    if L!="":
       boxl=float(L)
    falseword=word(x1)
    falseword.youngtableau().visual(boxl)
    print(youngwordstring)
    
    
    
def vis_equiv():
    x1 = str(entry1.get())
    
    falseword=word(x1)
    youngwordstring=(" ").join(falseword.youngtableau().word().char)
    print(youngwordstring)
    
    label3 = tk.Label(root, text= 'oops, your word does not represent a young tableau. However, it is equivalent to the following word:',font=('helvetica', 10))
    canvas1.create_window(400, 250, window=label3)
    
    label4 = tk.Label(root, text= youngwordstring,font=('helvetica', 10, 'bold'))
    canvas1.create_window(400, 275, window=label4)
    
    label5 = tk.Label(root, text= "Would you like to visualise the equivalent word?",font=('helvetica', 10, 'bold'))
    canvas1.create_window(400, 295, window=label5)
    
    canvas1.create_window(375, 330, window=button_vis_new_yes)
    canvas1.create_window(425, 330, window=button_vis_new_no)

def visualise ():
    boxl=1
    try:
        x1 = str(entry1.get())                  #############################
        L=entrybox.get()
        if L!='':
            boxl=float(L)

        young=youngtableau(x1)
        young.visual(boxl)

    except:
        vis_equiv()



def mult_setup():
    word1_entry.delete(0, 'end')
    word2_entry.delete(0, 'end')
    
    base()
    canvas1.create_window(400, 100, window=mult_text)
    canvas1.create_window(250, 130, window=word1_entry)
    canvas1.create_window(550, 130, window=word2_entry)
    canvas1.create_window(400, 170, window=button_mult)
    
    canvas1.create_window(400, 400, window=button_reset)

    
    
    word1_entry.focus_set()


def mult():
    word1=str(word1_entry.get())
    word2=str(word2_entry.get())

    prod_word=word(word1+" "+word2)
    youngword=prod_word.youngtableau().word()
    mult_result_word=(" ").join(youngword.char)
    print(mult_result_word)
    mult_result=tk.Label(root,text="The correct young tableau word is:\n"+mult_result_word+"\n Would you like to visualise it?",font=('helvetica', 10, 'bold'))
    canvas1.create_window(400, 220,window=mult_result)
    entry1.delete(0, 'end')
    entry1.insert(0,mult_result_word)
    canvas1.create_window(400, 280, window=button_vis)



def reset():
    base()
    canvas1.create_window(400, 80, window=label2)
    entry1.delete(0, 'end')
    entrybox.delete(0,'end')

    canvas1.create_window(400, 120, window=entry1)
    canvas1.create_window(400, 180, window=entrybox)

    canvas1.create_window(400, 160, window=boxlength_text)



    canvas1.create_window(400, 220, window=button_vis)
    
    canvas1.create_window(300, 450, window=button_equiv_setup)
    canvas1.create_window(500, 450, window=button_mult_setup)
    canvas1.create_window(290, 400, window=button_random_setup)
    canvas1.create_window(532, 400, window=button_random_equiv_setup)
    
    
    
    entry1.focus_set()
    
    
    












"""
BUTTONS

"""
        
button_vis = tk.Button(text='Visualise', command=visualise, bg='green', fg='white', font=('helvetica', 9, 'bold'))
    
button_vis_new_yes = tk.Button(text='Yes', command=vis_new, bg='green', fg='white', font=('helvetica', 9, 'bold'))
button_vis_new_no = tk.Button(text='No', command=reset, bg='red', fg='white', font=('helvetica', 9, 'bold'))

button_equiv = tk.Button(text='Check', command=check_equiv, bg='green', fg='white', font=('helvetica', 9, 'bold'))
button_reset=tk.Button(text='Back', command=reset, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button_equiv_setup=tk.Button(text="Check equivalency of words",command=check_equiv_setup, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button_mult_setup=tk.Button(text="Multiply young tableaus",command=mult_setup, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button_mult=tk.Button(text="Multiply",command=mult, bg='green', fg='white', font=('helvetica', 9, 'bold'))

button_random_setup=tk.Button(text="Create a random young tableau",command=random_YT_setup, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button_random_equiv_setup=tk.Button(text="Create a random equivalent tableau",command=random_k_setup, bg='brown', fg='white', font=('helvetica', 9, 'bold'))

button_create_random= tk.Button(text='Create a random young tableau', command=create_random_YT, bg='green', fg='white', font=('helvetica', 9, 'bold'))
button_create_equiv= tk.Button(text='Show random equivalent', command=create_random_equiv, bg='green', fg='white', font=('helvetica', 9, 'bold'))


reset()



root.mainloop()
























