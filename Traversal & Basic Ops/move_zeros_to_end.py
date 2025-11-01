"""This function moves all the zeros in the array to the end, maintaing the relative order of the non-zero elements. This space complexity is O(1)"""
def move_zeros_to_end(arr):
  l = 0
  for r in range(len(arr)):
    if arr[r] != 0:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
  return arr
