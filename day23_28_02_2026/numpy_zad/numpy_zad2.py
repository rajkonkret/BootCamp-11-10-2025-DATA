import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# wymiary tablic
print(a.ndim)  # 0
print(b.ndim)  # 1
print(c.ndim)  # 2
print(d.ndim)  # 3

arr = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr)  # [[[[[1 2 3 4 5]]]]]
print("Wymiar:", arr.ndim)  # Wymiar: 5

# odczytaie elementów z tablicy po indeksie
print(b)
print(b[0])  # 1
print(b[2])  # 3

# wypisac tablice c
# pierwszy wiersz
# pierwszy wiersz, drugi element
print(c)
print("Pierwszy wiersz:", c[0])  # Pierwszy wiersz: [1 2 3]
print("Pierwszy wiersz, drugi element:", c[0][1])  # Pierwszy wiersz, drugi element: 2
print(c[0, 1])  # 2, podejscie numpy

arr_10 = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
print(arr_10)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
# 4 element, wiersz 2
print("Czwarty element, wiersz 2:", arr_10[1, 3])
# Czwarty element, wiersz 2: 9

print(25 * "-")
arr_12_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_12_3d)
# -------------------------
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

print(10 * "-")
print(arr_12_3d[0])
# ----------
# [[1 2 3]
#  [4 5 6]]

print(10 * "-")
print(arr_12_3d[0, 1])
# ----------
# [4 5 6]

print(10 * "-")
print(arr_12_3d[0, 1, 2])
# ----------
# 6

print(10 * "-")
# indeksy ujemny
print(arr_10)

print("Wiersz indeks 1, ostatni element:", arr_10[1, -1])
# ----------
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
# Wiersz indeks 1, ostatni element: 10
