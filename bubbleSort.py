import time  

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1): 
        for j in range(0, n-i-1):  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]

start = time.perf_counter() 
bubbleSort(arr)
end = time.perf_counter() 
print("Sorted array is:", arr)
print(f"Time taken: {end - start:.6f} seconds")  
 