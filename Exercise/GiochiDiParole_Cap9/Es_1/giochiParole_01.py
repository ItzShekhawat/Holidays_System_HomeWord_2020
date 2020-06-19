# Scrivete un programma che legga il ﬁle words.txt
# e stampi solo le parole composte da più di 20 caratteri (caratteri spaziatori esclusi).

def findCharacters(): 
    filename = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\GiochiDiParole_Cap9\Ex_1\words.txt"

    fin = open(filename, "r")


    for _ in fin:
        word = fin.readline()
        word = word.strip()
        if len(word) > 20:
            print(word)
            

findCharacters()




