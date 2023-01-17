#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number}", end=" ")
if number < 0:
    num = number % -10
if number >= 0:
    num = number % 10
if num > 5:
    print(f"is {num} and is greater than 5")
elif num < 6 and num != 0:
    print(f"is {num} and is less than 6 and not 0")
else:
    print("is 0 and is 0")
