"""
Se in una classe ci sono 23 studenti, quante probabilità ci sono che due di loro compiano gli anni lo stesso giorno? 
Potete stimare questa probabilità generando alcuni campioni a caso di 23 date e controllando le corrispondenze. 
Suggerimento: per generare date in modo casuale usate la funzione randint nel modulo random. 

"""

import random
import math

people = 23
daysPerYear = 365
chance = 100


def paradoxProbability():
    # Finding the not possibile match
    probability = 0.00
    percentage = 1.00
    for d in range(people):
        percentage = float(((365-d)/daysPerYear) * percentage)

    percentage = percentage*100

    probability = chance-percentage
    return probability


def provoTeoria(li):

    dateIndex = list()

    for e in li:
        count = 0
        for x in range(len(li)):
            if(e == li[x]):
                count += 1
                dateIndex.append(x)

        if count > 1:
            print("Date coincidenti tra persone : ")
            print(dateIndex)


if __name__ == "__main__":

    p = paradoxProbability()
    print("")
    print(
        f"The probability of getting two people in the room with the same birthday is : {p}\n")
    """
    li = list()
    for _ in range(people):
        date = random.randint(1, 365)
        li.append(date)
    
    print(li)
    print("\n")

    provoTeoria(li)

    """
