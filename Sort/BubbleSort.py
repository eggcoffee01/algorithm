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

array = [5,4,3,2,1]
print(array)
bubble_sort(array)
print(array)