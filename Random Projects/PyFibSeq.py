#Brandon Lo
#Fibbonnaci calculator
import decimal
from math import sqrt

def F(n):
    if n == 0: return 0
    if n == 1: return 1
    else:
        top = (1 + sqrt(5))**n - (1 - sqrt(5))**n
        bottom = 2**n * sqrt(5)
        return top/bottom


maximum = int(input("How many values of the Fib Sequence do you want to print up to?: "))
print (round(F(maximum)))
