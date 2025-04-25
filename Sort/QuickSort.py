def quick_sort(array, start, end):
  if (start >= end):
    return
  left = start
  right = end
  pivot = array[(start + end) // 2]
  while left <= right:
    while array[left] < pivot:
      left += 1
    while array[right] > pivot:
      right -= 1
    if left <= right:
      array[left], array[right] = array[right], array[left]
      left += 1
      right -= 1
  quick_sort(array, start, right)
  quick_sort(array, left, end)