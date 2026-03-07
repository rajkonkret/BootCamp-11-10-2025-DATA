import pandas as pd

df = pd.read_csv('data_with_date.csv')
print(df)

df.info()
# RangeIndex: 32 entries, 0 to 31
# Data columns (total 5 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  32 non-null     int64
#  1   Date      31 non-null     str
#  2   Pulse     32 non-null     int64
#  3   Maxpulse  32 non-null     int64
#  4   Calories  30 non-null     float64
# dtypes: float64(1), int64(3), str(1)
# memory usage: 1.4 KB

df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='mixed')
print(df.to_string())
# 26        60      20201226    100       120     250.0 2020-12-26
# errors='coerce' - gdy nie potrafi zamienic (NaN) na datę wstawi NaT ( Not a Time)
# format='mixed' - jeśłi data w innym formacie zmieni na własciwy - %y-%m-%d

df = pd.read_csv('data_with_date.csv')
df.dropna(subset=['Date'], inplace=True)
print(df.to_string())
