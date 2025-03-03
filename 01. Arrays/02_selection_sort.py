# Selection sort an array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Go through the array to find the lowest value.
# Move the lowest value to the front of the unsorted part of the array. (swap with the 1st value)
# Go through the array again as many times as there are values in the array.


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selection_sort(my_array))

# Time complexity O(n^2)
