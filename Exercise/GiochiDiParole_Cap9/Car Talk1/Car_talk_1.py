"""
    “Ditemi una parola inglese con tre lettere doppie consecutive. 
    Vi dò un paio di parole che andrebbero quasi bene, ma non del tutto. 
    Per esempio la parola “committee”, co-m-m-i-t-t-e-e. 
    Sarebbe buona se non fosse per la “i” che si insinua in mezzo. 
    O “Mississippi”: M-i-s-s-i-s-s-i-p-p-i. Togliendo le “i” andrebbe bene. 
    Ma esiste una parolachehatrecoppiedilettereugualiconsecutive,eperquantonesodovrebbeessere l’unica. 
    Magari ce ne sono altre 500, ma me ne viene in mente solo una. Qual è

"""

filename = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\GiochiDiParole_Cap9\words.txt"

def triplegroup(word):
    #past = word[0]
    val = False
    cont = 0
    l = 0
    while l < len(word)-1:
        if word[l] == word[l+1]:
            cont += 1
            if cont == 3:
                val = True
            l += 2
        else:
            l = l+1 - 2*cont
            cont = 0
    
    return val


with open(filename, "r") as fin:

    for row in fin:
        word = fin.readline()
        word = word.strip()
        if triplegroup(word):
            print(word)
        

    
        
         
        


