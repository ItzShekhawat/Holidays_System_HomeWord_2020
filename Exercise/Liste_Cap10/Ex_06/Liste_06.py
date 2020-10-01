"""
Esercizio 10.6. 
Due parole sono anagrammi se potete ottenerle riordinando le lettere di cui sono composte. 
Scrivete una funzione di nome anagramma che riceva due stringhe e restituisca True se sono anagrammi.

"""


def anagrammi(word1, word2):
    w1 = list(word1)
    w2 = list(word2)

    if len(w1) != len(w2):
        return False
    else:
        w1.sort()
        w2.sort()
        for index in range(len(w1)):
            if w1[index] != w2[index]:
                return False

    return True


if __name__=="__main__":
    word1 = "Roma"
    word2 = "mora"
    print(anagrammi(word1, word2))
    
