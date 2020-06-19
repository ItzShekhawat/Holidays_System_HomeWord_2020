"""
“Di recente ho fatto visita a mia madre, e ci siamo accorti che le due cifre che compongono la mia età, invertite ,formano la sua. 
Per esempio, se lei avesse 73 anni, io ne avrei 37. 
Ci siamo domandati quanto spesso succedesse questo negli anni, ma poi abbiamo divagato su altri discorsi senza darci una risposta.” 
“Tornato a casa, ho calcolato che le cifre delle nostre età sono state sinora invertibili per sei volte. 
Ho calcolato anche che se fossimo fortunati succederebbe ancora tra pochi anni, e se fossimo veramente fortunati succederebbe un’altra volta ancora. 
In altre parole, potrebbe succedere per 8 volte in tutto. 
La domanda è: quanti anni ho io in questo momento?”

"""


def reverseAge():
    diff  = 10
    
    c = 0
    while diff < 70:
        print(f"The Diff is : {diff}")
        s = 0
        while s <= 100 :
            sString = str(s).zfill(2)
            r = sString[::-1]
            #print(f"reverse :  {r}")
            if int(r) - s == diff: 
                print(s) 
                c +=1
            s += 1
        diff += 1
        if c >= 8 : 
            break


reverseAge()
        



