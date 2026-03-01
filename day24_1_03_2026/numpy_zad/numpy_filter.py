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

# arr = np.random.randint(0, 100, size=100)

# nowoczesniejsze podejscie do liczb losowych
rng = np.random.default_rng()
arr = rng.integers(0, 100, size=100)

mean_values = np.mean(arr)  # średnia
print(mean_values)  # 51.63
greather_than_mean = arr[arr > mean_values]
print("Średnia:", mean_values)
print("Wartości większe od średniej:", greather_than_mean)
# Średnia: 48.78
# Wartości większe od średniej: [92 95 63 53 52 90 52 52 55 89 68 68 50 83 80 70 95 91 55 78 74 97 49 96
#  82 53 55 70 69 86 52 55 92 90 89 79 96 74 79 64 94 76 49 80 65 94 86 66
#  81]

arr = np.array([1, 2, np.nan, 4, np.nan, 6, 7])
print(arr)  # [ 1.  2. nan  4. nan  6.  7.] nan -> None

filtered_arr = arr[~np.isnan(arr)]  # ~ negacja (not)
print("Tablica bez NaN:", filtered_arr)  # Tablica bez NaN: [1. 2. 4. 6. 7.]

arr = np.random.random((5, 5))
print(arr)
print(arr.shape)  # (5, 5)

# > 0.5
filtered_arr = arr[arr > 0.5]
print("Większa od 0.5", filtered_arr)
# Wiksza od 0.5 [0.93502587 0.51204677 0.91385536 0.6913071  0.88948388 0.96985012
#  0.77542171 0.66638097 0.85755861 0.65096074 0.82158018 0.62553447
#  0.649456   0.50999179]
print(filtered_arr.shape)
# Większa od 0.5 [0.69198843 0.983911   0.54352368 0.54318706 0.55779043 0.99247
#  0.96907896 0.91460931 0.8908536  0.64948891 0.58470349 0.89013183
#  0.74612299]
# (13,)
