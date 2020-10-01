"""
Esercizio10.4. 
Scrivete una funzione di nome tronca che prenda una lista, 
la modiﬁchi togliendo il primo e l’ultimo elemento, e restituisca None

"""

def decapita_start(t): del t[0]
def decapita_end(t): del t[len(t)-1]

def tronca(li):
    decapita_start(li)
    decapita_end(li)
    return None
    

if __name__ == "__main__":
    
    li = [1, 40, 949, 54, 0 ,0 ,1, 92, 11]
    print(f"Old list :{li} \n ")
    tronca(li)
    print(f"The modified List  : {li} \n")