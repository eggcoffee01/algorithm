def selection_sort(array):
  N = len(array)
  for i in range(N - 1):
    min_idx = i
    for j in range(i + 1 , N):
      if array[j] < array[min_idx]:
        min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i] 

arr = [5,5,3,2,1]
print(arr)
selection_sort(arr)
print(arr)