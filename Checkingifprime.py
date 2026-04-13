from math import sqrt

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, int(sqrt(number)) + 1):
        if (number % i) == 0:
            print( number, "number is not a prime number")
            break
    else:
        print( number, "number is a prime number")