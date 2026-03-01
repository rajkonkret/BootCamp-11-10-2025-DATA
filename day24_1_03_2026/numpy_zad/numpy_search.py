import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print(arr)  # [1 2 3 4 5 4 4]

# zwróc indeksy elementów, które spełniają warunek
x = np.where(arr == 4)
print(x)  # (array([3, 5, 6]),)

# tablica liczb  do 10
# wypisac indeksy na których znajdują sie liczby parzyste

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = np.where(arr % 2 == 0)
print(x)  # (array([1, 3, 5, 7, 9]),) indeksy na których znajdują się liczby parzyste

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)  # 1 - indeks na który mogę wstawić wartość 7 zachowując sortowanie, wstawi sie po lewej stronie

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 8, side="right")
print(x)  # 3 indeks 3
arr = np.insert(arr, 3, 8)
print(arr)  # [6 7 8 8 9]
