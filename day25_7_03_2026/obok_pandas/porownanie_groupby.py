import time
import dask.dataframe as dd
import pandas as pd
import polars as pl
import platform, sys

filename = 'bigfile_polars.csv'

print("executable:", sys.executable)
print("machine:", platform.machine())  # arm64 albo x86_64
print("architecture:", platform.architecture())

start = time.time()
df = pd.read_csv(filename)
result = df.groupby('category')['value'].sum()
print("Pandas groupby:", result)
print("Czas:", time.time() - start)  # Czas: 13.816066265106201

start = time.time()
df = pl.read_csv(filename)
result = df.group_by('category').agg(pl.col("value").sum())
print("Polars groupby:", result.to_pandas())
print("Czas:", time.time() - start)  # Czas: 2.5797770023345947

# polars lazy scan
start = time.time()

result = (
    pl.scan_csv(filename)
    .group_by("category")
    .agg(pl.col("value").sum())
    .collect()  # bez tego nie uruchomi się zadanie
)
print("Polars groupby:", result.to_pandas())
print("Czas:", time.time() - start)  # Czas: 3.360197067260742
