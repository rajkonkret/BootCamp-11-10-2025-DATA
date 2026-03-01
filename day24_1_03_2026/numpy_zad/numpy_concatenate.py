import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)  # [1 2 3 4 5 6]

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1)
# [[1 2]
#  [3 4]]
print(arr2)
# [[5 6]
#  [7 8]]
arr = np.concatenate((arr1, arr2))
print(arr)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

arr = np.concatenate((arr1, arr2), axis=1)  # ułożone w poziomie
print(arr)
# [[1 2 5 6]
#  [3 4 7 8]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack([arr1, arr2])  # wierszowo
print(arr)
# [[1 2 3]
#  [4 5 6]]

arr = np.stack([arr1, arr2], axis=1)  # kolumnowo
print(arr)
# [[1 4]
#  [2 5]
#  [3 6]]

arr = np.hstack([arr1, arr2])
print(arr)  # [1 2 3 4 5 6]

arr = np.vstack([arr1, arr2])
print(arr)
# [[1 2 3]
#  [4 5 6]]

arr = np.dstack([arr1, arr2])  # głębokosc, dodaje 3 wymiar
print(arr)
# [[[1 4]
#   [2 5]
#   [3 6]]]

# sprawdzic kształt
print(arr.shape)  # (1, 3, 2)
