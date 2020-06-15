"""
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""

def find_it(lista):
    l = []
    lista.sort()
    for i in lista:
        if len(l) == 0 or i in l:
            l.append(i)
    if len(l)%2 != 0:
        return l[0]
    else:
        return find_it(lista[len(l):])

