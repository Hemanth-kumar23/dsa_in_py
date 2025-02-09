import time
start=time.perf_counter()
def selectionSort(array):
    n = len(array)
    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            if (array[j] < array[minimum]):
                minimum = j

        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

    return array

array = [13, 4, 9,45,12]
print("sortedlist =",selectionSort(array))
end=time.perf_counter()
print("the time is:",end-start)
