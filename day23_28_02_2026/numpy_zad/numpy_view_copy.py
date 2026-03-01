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
print(view.base is arr)  # True

