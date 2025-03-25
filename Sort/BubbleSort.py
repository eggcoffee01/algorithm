def bubble_sort(array):
  N = len(array)
  for i in range(N - 1):
    swapped = False
    for j in range(N - 1 - i):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        swapped = True
    if not swapped:
      break

arr = [5,4,3,2,1]
print(arr)
bubble_sort(arr)
print(arr)