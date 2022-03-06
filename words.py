# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:06:42 2019

@authors: Megi, Mino, Jacob
"""

# import subprocess

def parse_word(v):
    """
    Die Funktion parse_word erhält einen String.
    Falls dieser aus ganzen Zahlen getrennt von einem leerzeichen besteht,
    und die Zahlen jeweils die Zeilen in absteigender Reihenfolge eines Young Tableauxs
    ergeben, so wird ein Young Tableaux als Liste von Listen zurückgegeben.
    Falls der String nicht aus ganzen Zahlen besteht, oder kein Young Tableaux darstellt,
    wird der ValueError ("no young tableau") ausgelöst.
    """
    if v=="":
        return []
    #leeres young tableaux
    young=[[]]
    
    #lnum speichert die zuvor gelesene Nummer
    lnum=0
    #i speichert den index der Zeile des Tableauxs, in die momentan eingefügt wird
    i=0
    #splitte den string an Leerzeichen, also bei korrekter Eingabe in ganze Zahlen
    for el in v.split(" "):
        #falls der aktuelle Teil des Strings eine (möglicherweise rationale) Zahl ist,
        #wird sie in cnum abgespeichert, sonst ein Fehler ausgelöst
        try:
            cnum=int(el)
        except:
            raise ValueError ("no young tableau")
        #überprüfe ob die Zahl eine ganze war, falls nicht, wird ein fehler ausgelöst    
        if cnum!=float(el) or cnum<1:
            raise ValueError ("no young tableau")

        #falls die aktuelle Nummer kleiner ist als die vorherige, muss eine neue Zeile beginnen,
        #da die Zahlen in einer Zeile aufsteigen. Entsprechend wird eine neue Zeile angelegt und i erhöht.
        #Da alle Zahlen größer Null sind, ist die Bedingung im ersten Schritt nicht wahr.
        if cnum<lnum:
            young.append([])
            i+=1
        #einfügen der Zahl in die aktuelle Zeile und aktualisieren von lnum
        young[i].append(cnum)
        lnum=cnum
        
    #Anzahl der Zeilen im evtl. Tableaux
    height=len(young)
    
    #überprüfen ob die Zahlen in den Spalten strikt fallend sind durch vergleich jeder Zahl
    #mit der mit dem selben index eine zeile höher (beachte: Zeilen des Tableauxs in Reihenfolge von unten nach oben gespeichert)
    for j,level in enumerate(young):
        #Die oberste Zeile des Tableauxs ist immer korrekt, da die Zahlen keinen kleineren "Vorgänger" haben.
        #Daher soll die Überprüfung dor nicht stattfinden, und würde sonst einen Index Fehler hervorrufen
        if j!=height-1:
            for k, num in enumerate(level):
                #Falls die Zahlen einer Spalte nicht fallen, wird ein Fehler ausgelöst
                if young[j+1][k]>=num:
                    raise ValueError ("no young tableau")
        
    return young

def parse(row,file):
    """
    Die Funktion parse(row,file) liest die Zeile mit index "row" aus der Datei "file".
    Sofern diese Zeile ein Young Tableaux darstellt, wird dieses durch parse_word() zurückgegeben.
    Andernfalls erzeugt parse_word einen ValueError.
    """
    #Variable zum öffnen einer Datei mit Leserecht
    r=open(file,"r+")
    #Zeilen werden als Liste in line gespeichert
    lines=r.readlines()
    #dokument wird geschlossen
    r.close()
    
    """
    Alternativ:
    import linecache
    line=linecache.getline(file,row)
    
  
    """
    return parse_word(lines[row])



    




































