"""
Create a function named divisors/Divisors that takes an integer n > 1 and 
returns an array with all of the integer's divisors(except for 1 and the 
number itself), from smallest to largest. If the number is prime return the
string '(integer) is prime' (null in C#) (use Either String a in Haskell 
and Result<Vec<u32>, String> in Rust).

Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

"""

# way one, but the exit is not the official answer

def divisors(integer):
    l = []
    for i in range(2,integer):
        if(integer%i) == 0:
            l.append(i)
            
    if len(l) == 0:
        return print(("{0} is prime").format(integer))
    return l

# way two, official answer

def divisors(integer):
    lista = []
    for i in range(2,integer):
        if(integer%i) == 0:
            lista.append(i)
            
    if len(lista) == 0:
        return str(integer) + " is prime"
    return lista

# way 3 with kist comprehesion

def divisors(integer):
    lista = [a for a in range(2,integer) if integer%a == 0]
            
    if len(lista) == 0: return str(integer) + " is prime"
    return lista

