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


