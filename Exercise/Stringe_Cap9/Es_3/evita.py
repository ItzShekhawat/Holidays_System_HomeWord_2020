"""
Esercizio9.3. 
Scrivete una funzione di nome evita che richieda una parola e una stringa di lettere vietate, e restituisca True 
se la parola non contiene alcuna lettera vietata
"""

toxicLett = input("Insert a string o toxic Letters to avoid : >> ")
filename = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\GiochiDiParole_Cap9\words.txt"


def evita(word, toxicLett):
    val = True
    for letter in toxicLett:
        # print(letter)
        if word.find(''.join(letter)) != -1:
            val = False

    # print(str(val))
    return val

# Modiﬁcate poi il programma in modo che chieda all’utente di inserire una stringa di lettere vietate,
# e poi stampi il numero di parole che non ne contengono alcuna.
# Riuscite a trovare una combinazione di 5 lettere vietate che escluda il più piccolo numero di parole?


with open(filename, "r") as fin:
    for _ in fin:
        word = fin.readline()
        word = word.strip()
        if evita(word, toxicLett) == True:
            print(word)
