def insertion_sort(array):
  N = len(array)
  for i in range(1, N):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key