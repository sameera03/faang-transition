"""This function reverses an array in-place"""

def reverse_array(arr):
    lt, rt = 0, len(arr) - 1
    while lt < rt:
        arr[lt], arr[rt] = arr[rt], arr[lt]
        lt += 1
        rt -= 1
    return arr
