
import math
"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
length = len(numbers)

if length%2 != 0:
    half = length / 2
    index = math.ceil(half)
    print(numbers[index-1])
    #it is median-1 because list index starts at 0
else:
    half = math.ceil(length /2)
    median = (numbers[half-1]+numbers[half])/2
    print (median)
    


