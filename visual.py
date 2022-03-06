# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:06:42 2019

@authors: Megi, Mino, Jacob
"""
import subprocess
import os

def print_tex(young, boxlength=1,filename="youngtableau",grid="off"):
    if young==[]:
        raise ValueError ("cannot print empty young tableau")
    BASIS= \
           '\\documentclass{{article}}\n\n\
            \\usepackage{{tikz}}\n\
            \\usetikzlibrary{{calc}}\n\
            \\title{{Young Tableaux}}\n\
            \\begin{{document}}\n\
            \\maketitle\n\
            \\begin{{figure}}[h]\n\
               \\tikzset{{\n\
                  tick/.style = {{black, very thick}}\n\
                }}\n\
            \\begin{{tikzpicture}} % boxlength={0} \n\
            \{1} % draw rectangles and numbers, string created by def rectangle_nodes\n\
            \{2}\n\
            \\end{{tikzpicture}}\n\
            \\end{{figure}}\n\
            \\end{{document}}'
    

    maxlength=len(young[-1])
    height=len(young)
    
    if grid=="grid_on":
        gridstring= "% coordinates, for fixing bugs\n\
            \\draw[thin, gray, dotted ,step="+str(boxlength)+"] (0,0) grid ("+str(maxlength)+"*"+str(boxlength)+","+str(height)+"*"+str(boxlength)+");\n\
                \\foreach \z in {0,...,"+str(maxlength)+"} {\n\
                    \\draw[tick,black,thin] (\z*"+str(boxlength)+",-0.4) -- (\z*"+str(boxlength)+",-0.1);\n\
                    \\node at (\z*"+str(boxlength)+",-0.4) [below,black] { $\z$ };}\n\
                \\foreach \y in {1,2,...,"+str(height)+"} {\n\
                    \\draw[tick,black,thin] (-0.2,\y*"+str(boxlength)+") -- (-0.05,\y*"+str(boxlength)+");\n\
                    \\node at (-0.2,\y*"+str(boxlength)+") [left,black] { $\y$ };}"
    else:
        gridstring="%"
                
                                
    BASIS=BASIS.format(boxlength,rectangle_nodes(boxlength,young),gridstring)

    
    
    with open(filename+'.tex','w') as file:
        file.write(BASIS)
        file.close()

    subprocess.call(['pdflatex', filename+'.tex'])
    
        #windows only. gets confused, if file is already open
    os.startfile(filename+'.pdf')
        # windows (linux?). takes time. gets confused if file is already open.
    #subprocess.Popen(filename+'.pdf',shell=True)
        # linux only
    #subprocess.call(['xreader',filename+'.pdf'])
    
    
    print('Finished')
#    print(BASIS)
    
    




def rectangle_nodes(boxl,young):
    string=""
    for i,level in enumerate(young):
        for n, num in enumerate(level):
            string+="\n\\draw [ultra thick] ("+str(n*boxl)+","+str(i*boxl)+") rectangle ("+str(n*boxl+boxl)+","+str(i*boxl+boxl)+");\n\
                     \\node at ($("+str(n*boxl)+","+str(i*boxl)+")+("+str(0.5*boxl)+","+str(0.5*boxl)+")$) {$"+str(num)+"$};"
    return string[:] #mit [2:] schneidet pro zeile ab?
            
            


#for .format(): (boxlength, height of young tableaux, list of lengths of lines in the young tableaux)
















#   BASIS= \
#           '\\documentclass{{article}}\n\n\
#            \\usepackage{{tikz}}\n\
#            \\usetikzlibrary{{calc}}\n\
#            \\begin{{document}}\n\
#            \\begin{{figure}}\n\
#               \\tikzset{{\n\
#                  tick/.style = {{black, very thick}}\n\
#                }}\n\
#            \\begin{{tikzpicture}} % boxlength={0} \n\
#            \{1} % draw rectangles and numbers, string created by def rectangle_nodes\n\
#            % coordinates, for fixing bugs\n\
#            \\draw[thin, gray, dotted ,ystep=1,xstep={0}] (0,0) grid ({3}*{0},{2});\n\
#                \\foreach \z in {{0,...,{2}}} {{\n\
#                    \\draw[tick,black,thin] (\z*{0},-0.4) -- (\z*{0},-0.1);\n\
#                    \\node at (\z*{0},-0.4) [below,black] {{ $\z$ }};}}\n\
#                \\foreach \y in {{1,2,...,{3}}} {{\n\
#                    \\draw[tick,black,thin] (-0.2,\y) -- (-0.05,\y);\n\
#                    \\node at (-0.2,\y) [left,black] {{ $\y$ }};}}\n\
#            \\end{{tikzpicture}}\n\
#            \\end{{figure}}\n\
#            \\end{{document}}