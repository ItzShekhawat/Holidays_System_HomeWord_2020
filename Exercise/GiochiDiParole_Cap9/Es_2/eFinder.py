#Scrivete una funzione di nome niente_e che restituisca True se una data parola non contiene la lettera “e”. 
#Modiﬁcate il programma del paragrafo precedente in modo che stampi solo le parole dell’elenco prive della lettera “e”, e ne calcoli la percentuale sul totale delle parole.

def niente_e(word):
    value = False
    if word.find('e') == -1:
        value = True
    return value

filename = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\GiochiDiParole_Cap9\words.txt"
with open(filename, "r") as fin:

    for line in fin:
        word = fin.readline()
        word = word.strip()
        if niente_e(word) != True : 
            print(word)
        




    