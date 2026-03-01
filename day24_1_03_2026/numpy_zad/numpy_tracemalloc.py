import numpy as np
import tracemalloc

tracemalloc.start()
list1 = list(range(10_000_000))
list2 = list(range(10_000_000))

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Current memory usage: {current / 1024 ** 2} MB")
print(f"Peak memory usage: {peak / 1024 ** 2} MB")
