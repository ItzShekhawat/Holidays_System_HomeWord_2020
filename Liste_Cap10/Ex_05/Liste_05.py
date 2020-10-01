"""
Esercizio 10.5. 
Scrivete una funzione di nome ordinata che prenda una lista come parametro 
e restituisca True se la lista è ordinata in senso crescente, False altrimenti

"""

def ordinata(li):

    for index in range(len(li)-1):
        if(li[index] > li[index+1]):
            return False
            
    return True

if __name__=="__main__":
    li = [1, 2 , 4]
    print(f"The List looks like : {li}")

    val = ordinata(li)

    print(f"The Function is : {val}")

    