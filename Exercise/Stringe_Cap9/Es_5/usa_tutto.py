"""
Esercizio 9.5. 
Scrivete una funzione di nome usa_tutte che richieda una parola e una stringa di lettere richieste e che restituisca True 
se la parola utilizza tutte le lettere richieste almeno una volta. Quante parole ci sono che usano tutte le vocali aeiou? E aeiouy?
"""

sLett = input("Insert a string  : >> ")
filename = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\GiochiDiParole_Cap9\Es_2\words.txt"

def usa_tutte(word, sLett):
    val = False
    for letter in sLett:
        if word.find(''.join(letter)) != -1:
            val = True
    return val

with open(filename, "r") as fin:
    count = 0
    for line in fin:
        word = fin.readline()
        word = word.strip()
        if usa_tutte(word, sLett) == True : 
            print(word)
            count += 1

print(f"Number of words with {sLett} as component letters : {count}")