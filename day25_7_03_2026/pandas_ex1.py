# Pandas is a fast, powerful, and flexible open-source Python library used for data manipulation,
# analysis, and cleaning. It provides high-performance data structures—specifically
# Series (1D) and DataFrames (2D)

import pandas as pd

# pip install pandas
# pip install pandas==2.3.2

print(pd.__version__)  # 3.0.1 -> 2.3.2

# Series - odwzorowanie  kolumn
name_dict = {"name": ["Radek", "Tomek"]}

a = [1, 2, 3]  # jednowymiarowa, jako kolumna
my_var = pd.Series(a)
print(my_var)
# 0    1
# 1    2
# 2    3
# dtype: int64

print(my_var[0])  # 1

# nadanie nazw dla indeksów
my_var = pd.Series(a, index=["x", "y", "z"])
print(my_var)
# x    1
# y    2
# z    3
# dtype: int64
print(my_var['y'])  # 2, indeks po nowej nazwie

calories = {'day1': 420, "day2": 300, "day3": 390}
my_var = pd.Series(calories)
print(my_var)
# day1    420
# day2    300
# day3    390
# dtype: int64
