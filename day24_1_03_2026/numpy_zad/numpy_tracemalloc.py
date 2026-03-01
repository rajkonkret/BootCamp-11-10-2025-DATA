import numpy as np
import tracemalloc

# tracemalloc.start()
# list1 = list(range(1_000_000))
# list2 = list(range(1_000_000))
#
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
#
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# # Current memory usage: 762.9238739013672 MB
# # Peak memory usage: 762.9239883422852 MB
# # 1_000_000
# # Current memory usage: 76.27836608886719 MB
# # Peak memory usage: 76.27848052978516 MB

tracemalloc.start()
# list1 = list(range(1_000_000))
# list2 = list(range(1_000_000))

# array1 = np.arange(10_000_000, dtype=np.int64)
array1 = np.arange(1_000_000, dtype=np.uint8)
# array2 = np.arange(10_000_000, dtype=np.int64)
array2 = np.arange(1_000_000, dtype=np.uint8)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Current memory usage: {current / 1024 ** 2} MB")
print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# int64 10_000_000
# Current memory usage: 152.58807373046875 MB
# Peak memory usage: 152.58807373046875 MB

# int16 10_000_000
# Current memory usage: 38.14715576171875 MB
# Peak memory usage: 38.14715576171875 MB

# int8 10_000_000
# Current memory usage: 19.07366943359375 MB
# Peak memory usage: 19.07366943359375 MB

# int8 1_000_000 -128 do 127
# Current memory usage: 1.90753173828125 MB
# Peak memory usage: 1.90753173828125 MB

# uint8 1_000_000 0 do 255
# Current memory usage: 1.90753173828125 MB
# Peak memory usage: 1.90753173828125 MB
