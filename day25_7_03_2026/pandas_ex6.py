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

df = pd.read_csv('data.csv')
df.fillna({"Calories": 130}, inplace=True)
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

# superbezpieczne podejscie, zalecane pandas 3
df = pd.read_csv('data.csv')
df['Calories'] = df['Calories'].fillna(130)
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

# niebezpieczne !!!
# # od pandasa 3.0 to nie zmieni danych w oryginalnej DataFrame/Series
# df = pd.read_csv('data.csv')
# df['Calories'].fillna(130, inplace=True)
# print(df.loc[141])
# # Duration     60.0
# # Pulse        97.0
# # Maxpulse    127.0
# # Calories      NaN -> brak zmiany
# # Name: 141, dtype: float64

# mmean() - średnia arytmetyczna
df = pd.read_csv('data.csv')

x = df['Calories'].mean()
print("Średnia wynosi:", x)  # Średnia wynosi: 375.79999999999995

# zamian NaN w danych na wartości średnie
df['Calories'] = df['Calories'].fillna(x)
print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    375.8
# Name: 141, dtype: float64

# median() - mediana, wartość środkowa
data = {"Wiek": [25, 30, 35, 40, 45, 50, 55, 60, 65]}

df = pd.DataFrame(data)
mediana_wiek = df['Wiek'].median()
print("Mediana wieku:", mediana_wiek)  # Mediana wieku: 45.0

# wczytac data.csv
# oblizyć mediane na Calories
# wypełnic NaN wartością mediany
# sprawdzic wiersz 141

df = pd.read_csv('data.csv')
mediana_wiek = df['Calories'].median()
print("Mediana Kalorie:", mediana_wiek)  # Mediana Kalorie: 318.6
df['Calories'] = df['Calories'].fillna(mediana_wiek)
print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    318.6
# Name: 141, dtype: float64

# mode() - moda - dominanta - najczęciej występująca wartość
df = pd.read_csv('data.csv')
mode_calories = df['Calories'].mode()
print("NAjczęściej występująca (dominanta):", mode_calories)  # NAjczęściej występująca (dominanta): 0    300.0
df['Calories'] = df['Calories'].fillna(mode_calories[0])  # wyciagamy pierwszy element z listy
print(df.loc[141])
# NAjczęściej występująca (dominanta): 0    300.0
# Name: Calories, dtype: float64
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    300.0
# Name: 141, dtype: float64

# wyświeltenie wierszy zawierające NaN
df = pd.read_csv('data.csv')
print(df[df.isna().any(axis=1)])  # wiersze
#      Duration  Pulse  Maxpulse  Calories
# 17         45     90       112       NaN
# 27         60    103       132       NaN
# 91         45    107       137       NaN
# 118        60    105       125       NaN
# 141        60     97       127       NaN

# poszcegolne kolumny
print(df[df['Calories'].isna()])
#      Duration  Pulse  Maxpulse  Calories
# 17         45     90       112       NaN
# 27         60    103       132       NaN
# 91         45    107       137       NaN
# 118        60    105       125       NaN
# 141        60     97       127       NaN
