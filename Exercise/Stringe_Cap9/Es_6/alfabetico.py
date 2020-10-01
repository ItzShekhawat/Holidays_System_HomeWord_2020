"""
Esercizio9.6. 
Scrivete una funzione di nome alfabetica che restituisca True se le lettere di una parola compaiono in ordine alfabetico (le doppie valgono).
Quante parole “alfabetiche” ci sono?
"""

import string
filename = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\GiochiDiParole_Cap9\words.txt"


def alfabetica(word): 
    i = 0 
    while i < len(word)-1:
        if word[i+1] < word[i]:
              return False 
        i = i+1 

    return True

with open(filename, "r") as fin:
    count = 0
    for line in fin:
        word = fin.readline()
        word = word.strip()
        if alfabetica(word) == True : 
            print(word)
            count += 1

print(f"_")
