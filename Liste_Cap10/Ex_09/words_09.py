"""
Esercizio 10.9.
Scrivete una funzione che legga il file words.txt e crei una lista in cui ogni parola è un elemento.
Scrivete due versioni della funzione, una che usi il metodo appende una il costrutto t = t + [x].
Quale richiede più tempo di esecuzione? Perché?

"""


def fill_With_Append(file):
    li_Appent = list()

    for word in file:
        line = word.strip()
        li_Appent.append(line)
    print("List with append : ")
    print(li_Appent)


def fill_without_Append(file):
    index = 0
    li_Arrey = []
    for word in file:
        line = word.strip()
        li_Arrey = li_Arrey + [line]
        index += 1

    print("Arrey list : ")
    print(li_Arrey)


if __name__ == "__main__":

    path = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\Liste_Cap10\Ex_09\words.txt"
    file = open(path, "r")

    fill_without_Append(file)
    file.close()

    path = r"C:\Users\Karni\Desktop\School\System_Book\Exercise\Liste_Cap10\Ex_09\words.txt"
    file = open(path, "r")
    fill_With_Append(file)
    file.close()
