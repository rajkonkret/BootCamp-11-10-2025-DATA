import numpy as np

lista = [1, 2, 3, 4, 5]
print(lista[2:4])  # [3, 4]

# [start:stop] # [3, 4]

# indexy        0  1  2  3  4  5  6
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])  # [2 3 4 5]
print(arr[4:])  # [5 6 7]
print(arr[:4])  # [1 2 3 4]

print(arr[-1:-3])  # [] -> 6:4
print(arr[-3:-1])  # [5 6]
print(arr[-3:])  # [5 6 7]

# [start:stop:step]
print(arr[1:5:2])  # [2 4]
print(arr[::2])  # [1 3 5 7]

arr_10_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_10_2d)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

print(arr_10_2d[1, 1:4])  # [7 8 9]

print(arr_10_2d[0:2, 2])  # [3 8]

print(arr_10_2d[0:2, 1:4])
# [[2 3 4]
#  [7 8 9]]
