def merge_sort(array):
  if len(array) <= 1:
    return array
  mid = len(array) // 2
  left = merge_sort(array[:mid])
  right = merge_sort(array[mid:])
  return conquer(left, right) 
  
def conquer(left, right):
  array = []
  left_index, right_index = 0, 0
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      array.append(left[left_index])
      left_index += 1
    else:
      array.append(right[right_index])
      right_index += 1
  while left_index < len(left):
    array.append(left[left_index])
    left_index += 1
  while right_index < len(right):
    array.append(right[right_index])
    right_index += 1
  return array