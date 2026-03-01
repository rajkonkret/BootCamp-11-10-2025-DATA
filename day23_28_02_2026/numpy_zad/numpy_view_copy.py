import numpy as np

lista = [1, 2, 3, 4, 5]
lista2 = lista  # kopia adresu, referencji
print(lista2)
print(lista)
print(id(lista2))  # 4369254464
print(id(lista))  # 4369254464

lista_copy = lista.copy()
print(id(lista_copy))  # 4371536384

# kopia tabelki
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)  # [42  2  3  4  5]
print(x)  # [1 2 3 4 5]

print(id(x), id(arr))  # 4339655824 4339192560
print(x.base is arr)  # False, nie jest widokiem

# widok
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)  # [42  2  3  4  5]
print(x)  # [42  2  3  4  5], zmian ana obydwy tabelach

print(id(x), id(arr))  # 4461335280 4471645904
print(x.base is arr)  # True, jest widokiem do tabeli

arr = np.arange(10)
print(arr)  # [0 1 2 3 4 5 6 7 8 9]

view = arr[2:5]
print(view)
view[0] = 99
print(arr)
print(view)
# [ 0  1 99  3  4  5  6  7  8  9]
# [99  3  4]
print(view.base is arr)  # True, jest to widok

arr = np.arange(10)
copy = arr[::2]
copy[0] = 99
print(copy)
print(arr)
# [99  2  4  6  8]
# [99  1  2  3  4  5  6  7  8  9]
print(copy.base in arr)  # True, jest to widok

arr = np.arange(10)
copy = arr[::2]
copy[0] = 67
print(copy[0])  # 67
print(arr[0])  # 67

print(copy.base in arr)  # True, jest to widok

# reshape() - wskazuje kształt
arr = np.arange(1, 13)
print(arr)  # [ 1  2  3  4  5  6  7  8  9 10 11 12]
arr = np.arange(1, 13).reshape(3, 4)
print(arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

view_col = arr[:, 1].view()
print(view_col)  # [ 2  6 10]
view_col[:] = 99
print(arr)
# [[ 1 99  3  4]
#  [ 5 99  7  8]
#  [ 9 99 11 12]]

# kopia
copy_row = arr[0, :].copy()
copy_row[:] = 0
print(arr)
# [[ 1 99  3  4]
#  [ 5 99  7  8]
#  [ 9 99 11 12]]
print(copy_row)  # [0 0 0 0]
print(copy_row.base is arr)  # False nie jest widokiem, jest kopią

view_submatrix = arr[:2, :2].view()
view_submatrix *= 10
print(view_submatrix)
# [[ 10 990]
#  [ 50 990]]
print(arr)
# [[ 10 990   3   4]
#  [ 50 990   7   8]
#  [  9  99  11  12]]

lista = [1, 2, 3, 4, 5]
print(lista * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
lista_slice = lista[1:3]  # w listach pythonowych jest to kopia
print(lista_slice)
lista_slice[0] = 99
print(lista)  # [1, 2, 3, 4, 5]
print(lista_slice)  # [99, 3]
