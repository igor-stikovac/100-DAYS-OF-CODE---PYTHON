#is the number prime or not
import math

number = int(input("Which number do you want to check: "))
ind = True

if number < 2:
    ind = False
else:
    for i in range (2,int(math.sqrt(number))+1):
        if number % i == 0:
            ind = False
            break

if ind:
    print("Number is prime!\n")
else:
    print("Number is not prime!\n")