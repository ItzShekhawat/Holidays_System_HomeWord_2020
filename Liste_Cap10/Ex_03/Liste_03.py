"""
Esercizio 10.3. 
Scrivete una funzione di nome mediani che prenda una lista e restituisca una nuova lista 
che contenga tutti gli elementi, esclusi il primo e l’ultimo. 

"""
def decapita_start(t): del t[0]
def decapita_end(t): del t[len(t)-1]

def mediani(li):
    newList = [x for x in li]
    
    decapita_start(newList)
    decapita_end(newList)
    return newList
    

if __name__ == "__main__":
    li = [1, 2, 4, 5 ,75, 99, 0]
    newList = mediani(li)
    print(f"The previous list : {li} \n")
    print(f"The New List is : {newList} \n")

