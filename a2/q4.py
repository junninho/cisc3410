# define function that accepts a list as a parameter

def selection_sort(arr):
  # for loop value of length of the array
  for i in range(len(arr)):

    index_min = i

    for j in range(i+1, len(arr)):
      if (arr[j] < arr[index_min]): # if current value is less than minimum index reassign value
        index_min = j
    
    # assign array at index to minimum index and vice versa
    arr[i], arr[index_min] = arr[index_min], arr[i]

  return arr # return sorted array

test = [23, 12, 7, 3, 54, 33, 2, 49, 11] # test array
print(selection_sort(test)) # call function and print results