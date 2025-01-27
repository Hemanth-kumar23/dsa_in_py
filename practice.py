# def pivot(arr, start, end):
#     pivot = arr[start]
#     low = start + 1
#     high = end

#     while True:
#         while low <= high and arr[high] >= pivot:
#             high = high -1

#         while low <= high and arr[low] <= pivot:
#             low = low + 1

#         if low <= high:
#             arr[low], arr[high] = arr[high], arr[low]
#         else:
#             break
#     array[start], array[high] = array[high], array[start]
 
#     return high
 
# def quick_sort(array, start, end):
#     if start >= end:
#         return
 
#     # Call pivot 
#     p = pivot(array, start, end)
#     # Recursive call on left half
#     quick_sort(array, start, p-1)
#     # Recursive call on right half
#     quick_sort(array, p+1, end)
 
# array = [5, 1, 3, 9, 8, 2, 7]
# quick_sort(array, 0, len(array) - 1)

# # Output the sorted array
# print(array)


def lineraSerach(list, n, key):
    for i in range (0, n):
        if(list[i] == key):
            return i
    return -1
    
list = [1, 3, 5, 4, 7, 9]
key = 3

n = len(list)
res = lineraSerach(list ,n , key)
if(res == -1):
    print("element is not found ")
else:
    print("Element found at index :",res)