#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = number
if number < 0:
    num2 = number * -1
num1 = num2 % 10
if number < 0:
    num1 = num1 * -1
if (num1 > 5):
    print(f"Last digit of {number} is {num1} \
and is greater than 5")
elif num1 == 0:
    print(f"Last digit of {number} is {num1} and is 0")
elif num1 < 6 and num1 != 0:
    print(f"Last digit of {number} is {num1} \
and is less than 6 and not 0")
