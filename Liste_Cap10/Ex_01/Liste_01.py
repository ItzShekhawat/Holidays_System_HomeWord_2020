"""
Esercizio10.1. Scrivete una funzione di nome somma_nidificata che prenda una lista di liste di numeri interi 
e sommi gli elementi di tutte le liste nidiﬁcate.

"""

def somma_nidificata(li):
    tot = 0
    try:
        for element in li:
            for i in range(len(element)):
                tot += element[i]
        return tot
        
    except:
        print("Error")
        return None

if __name__ == "__main__":
    li = [[2,3,4,5] , [4,5,6,7], [3], [23, 45, 58, 99, 19, 48, 913]]
    
    total  = somma_nidificata(li)
    print (f" The result is :  {total}")


    

    
        