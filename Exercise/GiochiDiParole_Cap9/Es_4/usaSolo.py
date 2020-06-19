"""
Esercizio 9.4. 
Scrivete una funzione di nome usa_solo che richieda una parola e una stringa di lettere, e che restituisca True 
se la parola contiene solo le lettere indicate. 
Riuscite a comporre una frase in inglese usando solo le lettere acefhlo? Diversa da “Hoe alfalfa”?
"""

onlyLet = input("Insert a string : >> ")
filename = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\GiochiDiParole_Cap9\Es_2\words.txt"

def usa_solo(word, onlyLet):
    val = False
    for letter in onlyLet:
        #print(letter)
        if word.find(''.join(letter)) == -1:
            val = True
    return val

with open(filename, "r") as fin:
    for line in fin:
        word = fin.readline()
        word = word.strip()
        if usa_solo(word, onlyLet) == True : 
            print(word)

# Frase con acefhlo = Hello fallo


