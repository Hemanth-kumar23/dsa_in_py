def pivot(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high = high -1

        while low <= high and arr[low] <= pivot:
            low = low + 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    