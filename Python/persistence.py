"""
Attention!!!!! This exercise has been modified for educational purposes, 
the result is the last number resulting from consecutive products

Write a function, persistence, that takes in a positive parameter num and returns its 

multiplicative persistence, which is the number of times you must multiply the digits in num until 
you reach a single digit.

For example:

persistence(39) === 3 // because 3*9 = 27, 2*7 = 14, 1*4=4
                       // and 4 has only one digit
"""


def persistence(number):
    str_num = str(number)
    produto = 1
    count = 0
    new_list = []
    l = [int(indice) for indice in str_num]
    for y in l:
        produto *= y
        count = count + 1
    new_list.append(produto)
    if new_list[0] > 9:
        return persistence(new_list[0])
    else:
        return new_list