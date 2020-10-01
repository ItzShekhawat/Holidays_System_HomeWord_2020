"""
Esercizio 10.7
Scrivete una funzione di nome ha_duplicati 
che richieda una lista e restituisca True se contiene elementi che compaiono più di una volta.
Non deve modiﬁcare la lista di origine.
"""


def ha_duplicati(li):

    for index in li:
        count = 0
        for i in range(len(li)):
            if(index == li[i]):
                count += 1

        if count > 1:
            return True

    return False


def ha_duplicati_Fast(li):   # Metodo piu rapido

    if len(li) == len(set(li)):  # If there are duplic, the len won't be the same using set
        return False

    return True


if __name__ == "__main__":
    li = [1, 1, 3, 4, 5]

    print(ha_duplicati(li))
