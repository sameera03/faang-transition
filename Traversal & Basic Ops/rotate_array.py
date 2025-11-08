def rotate_array_right(arr, k):
  n = len(arr)
  k %= n

  def reverse_arr(l, r):
    while l < r:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1
  reverse(0, n-1)
  reverse(0, k-1)
  reverse(k, n-1)

  return arr


def rotate_array_left(arr, k):
  n = len(arr)
  k %= n

  def reverse_arr(l, r):
    while l < r:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1
  reverse(0, n-1)
  reverse(0, n-k-1)
  reverse(n-k, n-1)
  return arr

def rotate_array_left_2(arr, k):
  k = n- (k%n)
  arr = rotate_array_right(arr, k)
  return arr
