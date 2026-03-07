import pandas as pd

# data cleaning

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
#  3   Calories  164 non-null    float64 -> brak danych
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB

new_df = df.dropna()  # dane bez NaN
print(new_df.to_string())
new_df.info()
# <class 'pandas.DataFrame'>
# Index: 164 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  164 non-null    int64
#  1   Pulse     164 non-null    int64
#  2   Maxpulse  164 non-null    int64
#  3   Calories  164 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 6.4 KB

# zmieni w oryginalnej DataFrame
df.dropna(inplace=True)  # inplace - zmień oryginał
df.info()
# <class 'pandas.DataFrame'>
# Index: 164 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  164 non-null    int64
#  1   Pulse     164 non-null    int64
#  2   Maxpulse  164 non-null    int64
#  3   Calories  164 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 6.4 KB
