import time
import dask.dataframe as dd
import pandas as pd
import polars as pl

filename = "bigfile_polars.csv"

# polars
start = time.time()
df_polars = pl.read_csv(filename)
filtered_polars = df_polars.filter(pl.col("category") == "B")
print("Polars: liczba wierszy z kategorią 'B':", filtered_polars.height)
print("Polars filter time:", time.time() - start)
# Polars: liczba wierszy z kategorią 'B': 24997100
# Polars filter time: 6.70575213432312

# polars scan
start = time.time()

df_polars = pl.scan_csv(filename)

filtered_polars = df_polars.filter(pl.col("category") == "B").collect()
print("Polars: liczba wierszy z kategorią 'B':", filtered_polars.height)
print("Polars filter time:", time.time() - start)
# Polars: liczba wierszy z kategorią 'B': 24997100
# Polars filter time: 3.260093927383423

# pandas
start = time.time()
df_pandas = pd.read_csv(filename)
filtered_pandas = df_pandas[df_pandas['category'] == 'B']
print("Pandas: liczba wierszy z kategorią 'B':", len(filtered_pandas))
print("Pandas filter time:", time.time() - start)

# Polars: liczba wierszy z kategorią 'B': 24997100
# Polars filter time: 5.036498069763184
# Polars: liczba wierszy z kategorią 'B': 24997100
# Polars filter time: 3.5024619102478027
# Pandas: liczba wierszy z kategorią 'B': 24997100
# Pandas filter time: 21.906017065048218

# dask