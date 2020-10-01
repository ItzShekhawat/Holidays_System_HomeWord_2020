"""
Esercizio 11.3.
Applicate la memoizzazione alla funzione di Ackermann dell’Esercizio 6.2  e provate a 
vedere se questa tecnica rende possibile il calcolo della funzione con argomenti più grandi.

"""

# La risposta è no!!


def Ackermann(x, y):

    if x == 0:
        return y + 1
    elif x > 0 and y == 0:
        return Ackermann(x - 1, 1)
    elif x > 0 and y > 0:
        return Ackermann(x - 1, Ackermann(x, y - 1))


print(Ackermann(1, 7))
