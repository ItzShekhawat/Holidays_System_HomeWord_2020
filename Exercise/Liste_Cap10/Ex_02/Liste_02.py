"""
Esercizio 2
Scrivete una funzione di nome somma_cumulata che prenda una lista di numeri e restituisca la somma cumulata, 
cioè una nuova lista dove l’i-esimo elemento è la somma dei primi i+1 elementi della lista di origine

"""

def somma_cumulata(li):
    newList = list()
    for element in range(len(li)):
        add = 0
        if element == 0:
            newList.append(li[element])
        else:
            for i in range(element+1):
                add = li[i] + add
            newList.append(add)
            
    return newList
        

if __name__ == "__main__":
    li = [2, 2, 3, 4, 5, 15 , 67, 86]
    new_List = somma_cumulata(li)
    print("\n")
    print(f'The new List of accomiulo is : {new_List} \n')
