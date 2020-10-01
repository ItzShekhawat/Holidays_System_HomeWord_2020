"""
Esercizio 10.10.
Per controllare se una parola è contenuta in un elenco,  è possibile usare l’operatore in, ma è un metodo lento, 
perché ricerca le parole seguendo il loro ordine.

Dato che le parole sono in ordine alfabetico, 
possiamo accelerare l’operazione con una ricerca binaria(o per bisezione), 
che è un po’ come cercare una parola nel vocabolario. 
Partite nel mezzo e controllate se la parola che cercate viene prima o dopo la parola di metà elenco. 
Se prima, cercherete nella prima metà nello stesso modo, se dopo, cercherete nella seconda metà.
Ad ogni passaggio, dimezzate lo spazio di ricerca.  
Se l’elenco ha 113.809 parole, ci vorranno circa 17 passaggi per trovare la parola o concludere che non c’è.
Scrivete una funzione di nomebisezione che richieda una lista ordinata e un valore da ricercare, 
e restituisca True se la parola fa parte della lista, o False se non è presente

"""

from time import sleep


def nomebisezione(li_words, word):

    while True:
        #li_words = li_words.sort()
        middle = int(len(li_words)/2)

        if li_words[middle] == word:
            print(f"Trovato {word}")
            return True

        if len(li_words) <= 1:
            break

        if li_words[middle] > word:
            li_words = li_words[:middle]
            print(f"Minore : {li_words}")
        else:
            li_words = li_words[middle:]
            print(f"Maggiore : {li_words}")
        sleep(1)

    return False


if __name__ == "__main__":
    li_words = ["anna", "banana", "italy",
                "mario", "yuri", "zebra", "zzanzara"]
    word = input("Word to find : ")
    #word = "anna"
    print(nomebisezione(li_words, word))
