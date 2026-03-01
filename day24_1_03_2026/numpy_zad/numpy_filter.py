import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]

new_arr = arr[x]
print(new_arr)  # [41 43]

arr = np.array([41, 42, 43, 44])
filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

print(filter_arr)  # [False, False, True, True]
new_arr = arr[filter_arr]
print(new_arr)  # [43 44]

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
new_arr = arr[filter_arr]
print(filter_arr)  # [False False  True  True]
print(new_arr)  # [43 44]

arr = np.arange(21)
even = arr[arr % 2 == 0]  # modulo, reszta z dzielenia
print("Parzyste:", even)  # Parzyste: [ 0  2  4  6  8 10 12 14 16 18 20]
