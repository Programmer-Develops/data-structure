# Bubble Sort :- bubble sort is a simple sorting algorithm that repeatedly steps through the list,
#  compares adjacent elements and swaps them if they are in the wrong order.
#  The pass through the list is repeated until the list is sorted.
#  The algorithm gets its name from the way smaller elements "bubble" to the top of the list (beginning)
#  while larger elements sink to the bottom (end) with each pass.

'''
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped :
            break

arr = [2,5,1,4,6,8,10]
bubbleSort(arr)
print(arr)
'''


# Selection Sort :- selection sort is a simple sorting algorithm that divides the input list into two parts: the sorted part and the unsorted part.
#  Initially, the sorted part is empty and the unsorted part is the entire list.
#  The algorithm repeatedly selects the smallest (or largest, depending on sorting order) element from the unsorted part and moves it to the end of the sorted part.
#  This process continues until the entire list is sorted.

'''
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] <arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [2,5,1,4,6,8,10]
selectionSort(arr)
print(arr)
'''


# Insertion Sort :- insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.
#  It is much less efficient on large lists than more advanced algorithms such as quick sort, heap sort, or merge sort.
#  However, insertion sort provides several advantages:
#  - It is simple to implement.
#  - It is efficient for small data sets or partially sorted lists.
#  - It is stable (does not change the relative order of equal elements).
#  The algorithm works by dividing the list into a sorted and an unsorted part. Initially, the sorted part contains the first element, and the unsorted part contains the rest of the elements.
#  The algorithm iterates through the unsorted part, taking one element at a time and
#  inserting it into the correct position in the sorted part until the entire list is sorted.

'''
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
arr = [2,5,1,4,6,8,10]
insertionSort(arr)
print(arr)
'''


# Merge Sort :- merge sort is a divide-and-conquer algorithm that breaks down a list into smaller sublists until
#  each sublist contains a single element (which is inherently sorted).
#  Then, it repeatedly merges those sublists to produce new sorted sublists until there is only one sublist remaining,
#  which is the sorted list.

'''
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
arr = [2,5,1,4,6,8,10]
mergeSort(arr)
print(arr)
'''


# Quick Sort :- quick sort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and
#  partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
#  The sub-arrays are then sorted recursively.

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)
arr = [2,5,1,4,6,8,10]
sorted_arr = quickSort(arr)
print(sorted_arr)
