"""
Esercizio 11.1.
Scrivete una funzione che legga le parole in words.txte le inserisca come chiavi in un dizionario.
I valori non hanno importanza.
Usate poi l’operatore _in_ come modo rapido per controllare se una stringa è contenuta nel dizionario.
"""

from time import sleep


def fill_in_diz(key, diz):
    diz[key] = None             # Adding a new kay and give it none value
    # print(diz)


def chack_diz(fine_value, diz):

    if fine_value in diz:
        print("E presente")
    else:
        print("Non è presente")
    sleep(1)


if __name__ == "__main__":
    search = input("Find the key in the diz : ")
    path = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\Dizionari_Cap11\words.txt"
    fin = open(path, "r")
    diz = {}
    for el in fin:
        key = el.strip()
        fill_in_diz(key, diz)
        sleep(0)

    chack_diz(search, diz)

    print("Fine \n")
