"""
Leggete  la  documentazione  del  metodo  dei  dizionari set_defaulte  
usatelo  per scrivere una versione più concisa di inverti_diz.

"""


def inverti_diz(diz):
    inverse = {}
    for key in diz:
        val = diz[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == "__main__":
    diz = dict(k1=123, k2=134, k3=66, k4=123)
    print(inverti_diz(diz))
