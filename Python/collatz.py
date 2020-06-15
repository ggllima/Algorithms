def collatz(num):
    print(int(num),end=" ")
    if num <=1:
        return 1
    if num%2 == 0:
        return collatz(num/2)
    if num%2 != 0:
        return collatz(3*num+1)