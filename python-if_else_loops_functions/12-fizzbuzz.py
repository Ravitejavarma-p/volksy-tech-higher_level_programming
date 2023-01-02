#!/usr/bin/python3
for a in range(1, 101):
    if a % 5 == 0 and a % 3 == 0:
        print("FizzBuzz")
    elif a % 5 == 0:
        print("Buzz", end=" ")
    elif a % 3 == 0:
        print("Fizz", end=" ")
    print(a, end=" ")
