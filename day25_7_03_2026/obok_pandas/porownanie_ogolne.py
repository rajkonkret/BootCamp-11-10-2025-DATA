import time
import dask.dataframe as dd
import pandas as pd
import polars as pl

# ModuleNotFoundError: No module named 'pyarrow'
filename = "bigfile_polars.csv"

# pandas
start = time.time()
df = pd.read_csv(filename)
mean = df['value'].mean()
print("Pandas mean:", mean)
print("Czas:", time.time() - start)

# polars
start = time.time()
df = pl.read_csv(filename)
mean = df['value'].mean()
print("Pandas mean:", mean)
print("Czas:", time.time() - start)

# polars lazy, scan
start = time.time()

# wczytanie lazy - nie ładuje pliku
df = pl.scan_csv(filename)

mean = df.select(pl.col("value").mean()).collect()
mean_lazy = mean[0, 0]
print("Polars mean (lazy):", mean_lazy)
print("Czas:", time.time() - start)

# dask
star = time.time()
df = dd.read_csv(filename)
mean = df['value'].mean().compute()
print("Dask mean:", mean)
print("Czas:", time.time() - start)
# Pandas mean: 5000.35136653
# Czas: 25.86489486694336
# Pandas mean: 5000.35136653
# Czas: 3.1556200981140137
# Polars mean (lazy): 5000.35136653
# Czas: 1.899346113204956
# Dask mean: 5000.35136653
# Czas: 24.797860145568848
