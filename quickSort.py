def pivot(array, start, end): 
    pivot = array[start]
    low = start + 1
    high = end
 
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
  
        while low <= high and array[low] <= pivot:
            low = low + 1
 
        # Checking if low and high have crossed
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
 
    return high
 
def quick_sort(array, start, end):
    if start >= end:
        return
 
    # Call pivot 
    p = pivot(array, start, end)
    # Recursive call on left half
    quick_sort(array, start, p-1)
    # Recursive call on right half
    quick_sort(array, p+1, end)
 
array = [5, 1, 3, 9, 8, 2, 7]
quick_sort(array, 0, len(array) - 1)

# Output the sorted array
print(array)