import numpy as np

arr = np.arange(1, 13)
print(arr)  # [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(arr.dtype)  # int64
print(arr.shape)  # (12,) sprawdzenie kształt

new_arr = arr.reshape(4, 3)
print(new_arr)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print(new_arr.shape)  # (4, 3)

new_arr = arr.reshape(2, 3, 2)
print(new_arr)  #
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]
#
#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]
print(new_arr.shape)  # (2, 3, 2)
# dwie warstwy, trzy wiersze, dwie kolumny

# nie zgadza się liczba elementów
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# new_arr = arr.reshape(3, 3)
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/BootCamp-11-10-2025-DATA/day24_1_03_2026/numpy_zad/numpy_reshape.py", line 29, in <module>
#     new_arr = arr.reshape(3, 3)
# ValueError: cannot reshape array of size 8 into shape (3,3)

new_arr = arr.reshape(2, 2, -1)  # -1 - dostosowanie trzeciego wymiaru automatycznie
print(new_arr)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
print(new_arr.shape)  # (2, 2, 3)

# [1, 2, 3, 4, 5, 6, 7, 8]
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr = arr.reshape(2, 2, -1)
print(new_arr)
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
print(new_arr.shape)  # (2, 2, 2)

arr = np.arange(12)
print(arr)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]
new_arr = arr.reshape(-1, 2)
print(new_arr)
# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]]
print(new_arr.shape)  # (6, 2)

new_arr = arr.reshape(3, -1)
print(new_arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(new_arr.shape)  # (3, 4)
