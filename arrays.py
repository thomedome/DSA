# Usually a good idea to write down the steps to an algorithm before writing in a language so you have a decent mental map of how to properly write the algorithm.

import numpy
import os
os.system("cls")

dataset = numpy.random.randint(5000, size=100) # Max 5000, 100 Entries

minVal = dataset[0]

print("Unsorted Set:", dataset, "\n")

def getMinValLinear(set):
    for i in range(len(set) - 1):
        print("Comparing", set[i], "to", minVal)
        if set[i] < minVal:
            minVal = set[i]
            continue
        else:
            continue

    print("The lowest number from this dataset is:", minVal)


# Bubble Sort:
# Go through array one value at a time
# For each value, compare the value with the next value
# If the value is higher than the next one, swap the values so that the highest comes last
# Go thorugh the array as many times as there are values in the array

def bubbleSort(set):
    num = len(set)
    for i in range(num - 1): # Looping so that every number can bubble up
        for j in range(num - i - 1): # 1 "Bubble" to the top. num - i - 1 
            if set[j] > set[j + 1]:
                set[j] , set[j + 1] = set[j + 1], set[j]
    
    print("Ordered List:", set)

def bubbleSortImproved(set): # Stops swapping after one swap per inner loop. Makes for a more efficient loop
    num = len(set)
    for i in range(num - 1):
        swapped = False
        for j in range(num - i - 1):
            if set[j] > set[j + 1]:
                set[j], set[j + 1] = set[j + 1], set[j]
                swapped = True
        if not swapped:
            break
    
    print("Ordered List:", set)

bubbleSortImproved(dataset)