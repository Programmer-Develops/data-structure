# find sum, max, smallest and average of all elements of array and reverse and  forward array
import numpy as np

arr = np.array([1,2,3,6,8,9,4,5,6])

print(f"sum: {np.sum(arr)}, average: {np.average(arr)}")
print(f"max number: {np.max(arr)}, smallest number: {np.sort(arr)[0]}")
print(f"forward: {arr}, reverse: {arr[::-1]}")

# Linear search
x = int(input("enter the element you want to find : "))
l = 0 # pointer

while l < len(arr):
    if arr[l] == x:
        print(f"element {x} present at {l}th position") 
        break
    l += 1

if l >= len(arr):
    print("Element not found ")


# Binary Search

def binary(arr,x):
    low = 0
    high = len(arr)-1

    while low != high:
        mid = (low+high)//2

        if arr[mid] < x:
            low = mid +1
        elif arr[mid] > x:
            high = mid -1
        else:
            return mid
    return "Element not found"

