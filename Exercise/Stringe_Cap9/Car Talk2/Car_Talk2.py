"""

    “L’altro giorno stavo guidando in autostrada e guardai il mio contachilometri. 
    È a sei cifre, come la maggior parte dei contachilometri, e mostra solo chilometri interi. 
    Se la mia macchina, per esempio, avesse 300.000 km, vedrei 3-0-0-0-0-0.” 
    “Quello che vidi quel giorno era interessante. 
    Notai che le ultime 4 cifre erano palindrome, cioè si potevano leggere in modo identico sia da sinistra a destra che viceversa. 
    Per esempio 5-4-4-5 è palindromo, per cui il contachilometri avrebbe potuto essere 3-1-5-4-4-5” “Un chilometro dopo, gli ultimi 5 numeri erano palindromi. 
    Per esempio potrei aver letto 3-6-5-4-5-6. Un altro chilometro dopo, le 4 cifre di mezzo erano palindrome. 
    E tenetevi forte: un altro chilometro dopo tutte e 6 erano palindrome!” 

    “La domanda è: quanto segnava il contachilometri la prima volta che guardai?”

"""

#filename = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\GiochiDiParole_Cap9\words.txt"

def findPoloindromo():
    i = 100000
    while i < 1000000:
        c = 0              #  indicherà Polindromo di quante cifre 
        #print(i)
        li = [int(x) for x in str(i)]
        print(li)
        length = len(li)
        #print(length)
        for l in range(len(li)):
            if(li[l] == li[length-1]):
                c += 1
                s = l  #Start
                #print(s)
                f = length-1 #Final
                #print(f)
                while True:
                    if f <= l :
                        #print(str(li))
                        break

                    if li[s+1] == li[f]:
                        c += 1
                        s = s+1
                        f = f-1
                    else:
                        c = 0
                        break
            else:
                if(length == l):
                    l = len(li)
                else:
                    i= i+1
                    length -= 1 

        if(c != 0):
            print(li) 

        
                  

findPoloindromo()


