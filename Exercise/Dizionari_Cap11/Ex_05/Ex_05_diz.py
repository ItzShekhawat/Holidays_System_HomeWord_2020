"""
Esercizio 11.5.
Due parole sono “ruotabili” se potete far ruotare le lettere dell’una per ottenerel’altra
(vedere ruota_parola nell’Esercizio 8.5).
Scrivete  un  programma  che  legga  un  elenco  di  parole
e  trovi  tutte  le  coppie  di  parole  ruotabili.
"""


def ruotabili(li_word):
    """
    for word in range(len(li_word)-1):
        if(len(set(li_word[word])) == len(set(li_word[word+1]))):

    """
    return set(li_word)


if __name__ == '__main__':
    list_word = ["marco", "giovanni", "anna", "ocram"]

    print(ruotabili(list_word))
