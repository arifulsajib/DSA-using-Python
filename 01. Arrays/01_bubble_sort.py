# Bubble sort an array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# https: // www.w3schools.com/dsa/dsa_algo_bubblesort.php
# Go through the array, one value at a time.
# For each value, compare the value with the next value.
# If the value is higher than the next one, swap the values so that the highest value comes last. (If no swap happens, stop because the array is sorted).
# Go through the array as many times as there are values in the array.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


print(bubble_sort(my_array))

# Time complexity O(n^2)
