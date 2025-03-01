# Find The Lowest Value in an Array
my_array = [7, 12, 9, 4, 11]

# Algrorithms:
# Go through the values in the array one by one.
# Check if the current value is the lowest so far, and if it is, store it.
# After looking at all the values, the stored value will be the lowest of all values in the array.


def lowest_value(arr):
    lowest = arr[0]
    for x in arr:
        if x < lowest:
            lowest = x
    return lowest


print(lowest_value(my_array))

# Time complexity O(n) Linear
