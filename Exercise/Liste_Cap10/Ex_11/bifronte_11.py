"""
Esercizio 10.11.
Una coppia di parole è “bifronte” se l’una si legge nel verso opposto dell’altra.
Scrivete un programma che trovi tutte le parole bifronti nella lista di parole.
"""


def bifronti(li):
    for el in li:
        for index in range(len(li)-1):
            if el[::-1] == li[index+1]:
                print(f'{el} is a bifronte of : ')
                print(li[index+1])
                print("")

    return


if __name__ == '__main__':
    word_list = ["anna", "mario", "wonder", "oiram", "nisia", "luca", "vita"]

    bifronti(word_list)
