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
