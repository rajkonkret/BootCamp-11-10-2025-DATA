import pandas as pd

df = pd.read_csv('data.csv')
df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  164 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB

df.fillna(130, inplace=True)  # wpisanie 130 w miejsca NaN
df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  169 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB

print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    130.0
# Name: 141, dtype: float64
