#!/usr/bin/python3

def fizzbuzz():
    """prints the numbers from 1 to 100 separated by a space."""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            i = "Fizz"
        elif i % 5 == 0 and i % 3 != 0:
            i = "Buzz"
        elif i % 5 == 0 and i % 3 == 0:
            i = "FizzBuzz"
        print("{} ".format(i), end='')
