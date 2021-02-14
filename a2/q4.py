def selection_sort(arr):
  for i in range(len(arr)):

    index_min = i

    for j in range(i+1, len(arr)):
      if (arr[j] < arr[index_min]):
        index_min = j
    
    arr[i], arr[index_min] = arr[index_min], arr[i]

  return arr

test = [23, 12, 7, 3, 54, 33, 2, 49, 11]
print(selection_sort(test))