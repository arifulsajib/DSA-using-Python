# insertion sort an array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Take the first value from the unsorted part of the array.
# Move the value into the correct place in the sorted part of the array.
# Go through the unsorted part of the array again as many times as there are values.


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1, -1, -1):  # start from i-1 = 64(1st loop) untill 0 backword
            if arr[j] > current_value:  # 64>34
                arr[j+1] = arr[j]  # shift 64 to 34 position
                insert_index = j  # 34 will be inserted in 64 position
            else:
                break
        arr[insert_index] = current_value
    return arr


print(insertion_sort(my_array))
