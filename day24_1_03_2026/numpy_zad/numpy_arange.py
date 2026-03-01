import numpy as np

arr = np.arange(10)
print(arr)  # [0 1 2 3 4 5 6 7 8 9]
print(arr.dtype)  # int64

arr = np.arange(5, 23)
print(arr)  # [ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22]
print(arr.dtype)  # int64

arr = np.arange(0, 20, 2)  # start, stop, krok
print(arr)  # [ 0  2  4  6  8 10 12 14 16 18]
print(arr.dtype)  # int64

arr = np.arange(10, 0, -1)
print(arr)  # [10  9  8  7  6  5  4  3  2  1]

arr = np.arange(0, 10, -1)
print(arr)  # []

arr = np.arange(0, 1, 0.1)
print(arr)  # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

arr = np.arange(0, 5, dtype="float32")
print(arr)  # [0. 1. 2. 3. 4.]
print(arr.dtype)  # float32

arr = np.arange(1, 5, dtype="complex")  # liczby zespolone
print(arr)  # [1.+0.j 2.+0.j 3.+0.j 4.+0.j]
print(arr.dtype)  # complex128

arr = np.arange(0, 5, 0.5)
print(arr)  # [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]
print(arr.dtype)  # float64

arr = np.linspace(0, 1, 10)
print(arr)
# [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
#  0.66666667 0.77777778 0.88888889 1.        ]

arr = np.linspace(0, 1, num=10, endpoint=False)
print(arr)  # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

# retstep=True - podaj krok jaki zastosowałeś
arr, step = np.linspace(0, 1, num=5, retstep=True)
print("Tablica:", arr)  # Tablica: [0.   0.25 0.5  0.75 1.  ]
print("Krok:", step)  # Krok: 0.25

print(arr.shape)  # (5,)
