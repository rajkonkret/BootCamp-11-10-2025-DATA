import pandas as pd

df = pd.read_csv('marketing_r.csv',
                 sep=",",
                 parse_dates=['date_served',
                              'date_subscribed',
                              'date_canceled'])

print(df.head())
print(df['date_subscribed'].head())
# 0   2018-01-01
# 1   2018-01-01
# 2   2018-01-01
# 3   2018-01-01
# 4   2018-01-01
# Name: date_subscribed, dtype: datetime64[us]
