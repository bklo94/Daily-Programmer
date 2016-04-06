#Brandon Lo
#Pi calculator in python
import decimal

degrees = int(input("How many values of pi do you want to print?: "))

while degrees >= 50:
    print("Please select a number less than 50")
    degrees = int(input("How many values of pi do you want to print?: "))
    
else:
    sum = 0
    for i in range(0,10000):
        sum += ((-1)**i)/(2.0*i + 1.0)
    answer = 4 * sum
    print ('%.*f' % (degrees,answer))
