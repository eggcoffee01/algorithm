def selection_sort(array):
  N = len(array)
  for i in range(N - 1):
    min_idx = i
    for j in range(i + 1 , N):
      if array[j] < array[min_idx]:
        min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i] 

array = [5,4,3,2,1]
print(array)
selection_sort(array)
print(array)