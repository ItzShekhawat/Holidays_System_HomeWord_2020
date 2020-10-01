"""
Esercizio 11.4.
Se avete svolto l’Esercizio 10.7, avete già una funzione di nome ha_duplicati
che richiede come parametro una lista
e restituisce True se ci sono oggetti ripetuti all’interno della lista.
Usate un dizionario per scrivere una versione più rapida e semplice di ha_duplicati.

"""


def duplicate_dictionary_check(d):
    for val in d.values():
        count = 0
        if((val in d.values()) == True):
            count = count + 1
            if(count > 1):
                return False

    return True


me = {"name": "KarniSingh", "secondName": "Singh", "Surname": "Shekhawat"}
me2 = {"name": "KarniSingh ", "secondName": "Karni", "Surname": "Shekhawat"}


def duplici(m):

    return len(m.values()) == len(set(m.values()))


print(duplici(me))
