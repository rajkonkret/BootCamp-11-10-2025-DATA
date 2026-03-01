import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = np.array_split(arr, 3)
print(new_arr)  # [array([1, 2]), array([3, 4]), array([5, 6])]

new_arr = np.array_split(arr, 4)
print(new_arr)  # [array([1, 2]), array([3, 4]), array([5]), array([6])]
print(new_arr[0])  # [1 2]
print(new_arr[1])  # [3 4]
print(new_arr[2])  # [5]
print(new_arr[3])  # [6]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new_arr = np.array_split(arr, 3)
print(new_arr)
# [array([[1, 2],
#        [3, 4]]),
#        array([[5, 6],
#        [7, 8]]),
#        array([[ 9, 10],
#        [11, 12]])]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]])
new_arr = np.array_split(arr, 3)
print(new_arr)
# [array([[1, 2],
#        [3, 4],
#        [5, 6]]), array([[ 7,  8],
#        [ 9, 10],
#        [11, 12]]), array([[13, 14],
#        [15, 16],
#        [17, 18]])]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]])
new_arr = np.array_split(arr, 3, axis=1)
print(new_arr)
# [array([[ 1],
#        [ 3],
#        [ 5],
#        [ 7],
#        [ 9],
#        [11],
#        [13],
#        [15],
#        [17]]),
#        array([[ 2],
#        [ 4],
#        [ 6],
#        [ 8],
#        [10],
#        [12],
#        [14],
#        [16],
#        [18]]),
#        array([], shape=(9, 0), dtype=int64)]

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arr = np.hsplit(arr, 3)
print(new_arr)
# [array([[ 1],
#        [ 4],
#        [ 7],
#        [10],
#        [13],
#        [16]]), array([[ 2],
#        [ 5],
#        [ 8],
#        [11],
#        [14],
#        [17]]), array([[ 3],
#        [ 6],
#        [ 9],
#        [12],
#        [15],
#        [18]])]