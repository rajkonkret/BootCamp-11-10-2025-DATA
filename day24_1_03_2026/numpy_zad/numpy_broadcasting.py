# broadcasting
# zamienia eleemnty tablicy wg podanego wzoru automatycznie
# nie trzeba ręcznie wykonywac obliczenia na każdym elemencie
# jeśli wymiary tablic są równe jest ok
# jesli jeden z wymiarów wynoi 1, NumPy rozciąga ten wymiar by dostosowac do drugiej tablicy
# jeśli wymiary są różne i żaden nie wynosi 1 - otrzymamy bład!!!
import numpy as np

arr = np.array([1, 2, 3])
result = arr + 10  # -> [10, 10, 10]
print(result)  # [11 12 13]

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
print(arr1)
# [1 2 3]
print(arr2)
# [[10]
#  [20]
#  [30]]
print(arr1.shape)  # (3,)
print(arr2.shape)  # (3, 1)
result = arr1 + arr2
print(result)
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

arr1 = np.array([[[1, 2, 3], [4, 5, 6]]])
arr2 = np.array([10, 20, 30])
print(arr1)
# [[[1 2 3]
#   [4 5 6]]]
print(arr2)
# [10 20 30]
print(arr1.shape)  # (1, 2, 3)
print(arr2.shape)  # (3,)
result = arr1 + arr2
print(result)
# [[[11 22 33]
#   [14 25 36]]]

arr1 = np.ones((4, 3, 2))
print(arr1)
# [[[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]]

arr2 = np.array([10, 20])
result = arr1 + arr2
print(result)
#  [[11. 21.]
#   [11. 21.]
#   [11. 21.]]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20])
print(arr1.shape)  # (3,)
print(arr2.shape)  # (2,)
# result = arr1 + arr2
# print(result)
# ValueError: operands could not be broadcast together with shapes (3,) (2,)

# wykorzystanie reshape() do dostosowania danych tak by był możliwy broadcasting
arr1 = np.array([1, 2, 3]).reshape(3, 1)
arr2 = np.array([10, 20]).reshape(1, 2)
print(arr1.shape)  # (3, 1)
print(arr1)
# [[1]
#  [2]
#  [3]]
print(arr2.shape)  # (1, 2)
print(arr2)
# [[10 20]]
result = arr1 + arr2
print(34 * "-")
print(result)
# ----------------------------------
# [[11 21]
#  [12 22]
#  [13 23]]
print(result.shape)  # (3, 2)
