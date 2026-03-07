import pandas as pd

data = pd.read_csv('data_with_date.csv')
print(data)

# zamiana wartości
data.loc[7, "Duration"] = 45
print(data.loc[7])
# Duration              45
# Date        '2020/12/08'
# Pulse                104
# Maxpulse             134
# Calories           253.3
# Name: 7, dtype: object
