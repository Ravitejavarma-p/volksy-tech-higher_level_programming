#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst =  number % 10
if number < 0:
    last = last - 10
if last > 5:
    print("Last digit of", number, " is ", last, " and is greater than 5")
elif last == 0:
    print(Last digit of", number, " is ", last, " and is zero")
else:
    print("Last digit of", number, " is ", last, " and is greater than 6 and not 0")
