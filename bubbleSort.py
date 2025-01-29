def bubbleSort(array):
    
  # loop to access each array element
   for i in range(len(array)):

    # loop to compare array elements
      for j in range(0, len(array) - i - 1):
          
        if array[j] > array[j + 1]:
        
          temp = array[j]
          array[j] = array[j+1]
          array[j+1] = temp


list = [5,1,4,2,8]

bubbleSort(list)

print('Sorted Array in Ascending Order:')
print(list)