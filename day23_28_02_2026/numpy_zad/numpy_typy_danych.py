import numpy as np

arr = np.array([1, 2, 3, 4])

# odczytanie typu danych
print(arr.dtype)  # int64

print(np.iinfo(np.int64).max)
print(np.iinfo(np.int64).min)
# 9223372036854775807
# -9223372036854775808

# int16 -> 32767 -32768
# int8 -> -128 do 127
# uint8 = 0 do 255 be znaku, tylko wartości dodatnie

arr_str = np.array(['apple', 'banana', 'cherry'])
print(arr_str.dtype)  # <U6
# unicode, 6 znaków maksymalnie, < - little-endian

arr_own = np.array([1, 2, 3, 4], dtype="S")
print(arr_own.dtype)  # |S1
print(arr_own)  # [b'1' b'2' b'3' b'4'] jednobajtowe stringi

arr_i4 = np.array([1, 2, 3, 4], dtype='i4')
print(arr_i4)  # [1 2 3 4]
print(arr_i4.dtype)  # int32
print(np.iinfo(np.int32).max)
print(np.iinfo(np.int32).min)
# 2147483647
# -2147483648

# arr_err = np.array(['a', "2", "3"], dtype="i")
# ValueError: invalid literal for int() with base 10: 'a'

arr_float = np.array([1.1, 2.1, 3.1, 4.1])
print(arr_float)  # [1.1 2.1 3.1 4.1]
print(arr_float.dtype)  # float64

print(np.finfo(np.float64))
# tiny =       2.2250738585072014e-308
# max =        1.7976931348623157e+308

print(arr)
print(arr.dtype)
# [1 2 3 4]
# int64

new_arr = arr.astype("i")
print(new_arr.dtype)  # int32

new_arr = arr.astype(int)
print(new_arr)  # [1 2 3 4]
print(new_arr.dtype)  # int64

arr_bool = np.array((1, 0, 3))
new_arr_bool = arr_bool.astype(bool)
print(new_arr_bool)  # [ True False  True]
print(new_arr_bool.dtype)  # bool
