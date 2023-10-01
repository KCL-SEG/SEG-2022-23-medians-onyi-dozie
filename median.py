
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

length = len(numbers)

if length == 1:
    print (numbers[0])
elif length%2 != 0:
    half = length / 2
    print(f'printing out the first calculated half {half}')
    index = math.ceil(half)
    print(f'rounded up half {median}')
    print(f'the median of the list is {numbers[index-1]}')
    #it is median-1 because list index starts at 0
else:
    half = length /2
    print(f'half {half}')
    print (f' numbers[half-1] {numbers[half-1]}')
    print (f' numbers[half] {numbers[half]}')
    median = (numbers[half-1]+numbers[half])/2
    print (f'the median of this list is {median}')
    
#print(numbers)

