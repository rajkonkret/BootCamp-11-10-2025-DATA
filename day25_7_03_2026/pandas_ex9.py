# sprawdzenie duplikatów
import pandas as pd

df = pd.read_csv('data_with_date.csv')
print(df.to_string())

# sprawdzenie czy wiersze zawierają duplikaty, True - wiersz zduplikowany
print(df.duplicated())
# 11        60  '2020/12/12'    100       120     250.7
# 12        60  '2020/12/12'    100       120     250.7
# 11    False
# 12     True

# usunięcie duplikatów
df.drop_duplicates(inplace=True)
print(df.to_string())
# 11        60  '2020/12/12'    100       120     250.7
# 13        60  '2020/12/13'    106       128     345.3

print(df.duplicated())
