import numpy as np
import pandas as pd

# df = pd.read_csv('marketing_r.csv')
# print(df.head().to_string())

df = pd.read_csv('marketing_r.csv', sep=",")
print(df.head(1).to_string())

print(df.describe())
#            user_id date_served  ... subscribing_channel is_retained
# count        10037       10021  ...                1856        1856
# unique        7309          31  ...                   5           2
# top     a100000882     1/15/18  ...           Instagram        True
# freq            12         789  ...                 600        1279

df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 10037 entries, 0 to 10036
# Data columns (total 12 columns):
#  #   Column               Non-Null Count  Dtype
# ---  ------               --------------  -----
#  0   user_id              10037 non-null  str
#  1   date_served          10021 non-null  str
#  2   marketing_channel    10022 non-null  str
#  3   variant              10037 non-null  str
#  4   converted            10022 non-null  object
#  5   language_displayed   10037 non-null  str
#  6   language_preferred   10037 non-null  str
#  7   age_group            10037 non-null  str
#  8   date_subscribed      1856 non-null   str
#  9   date_canceled        577 non-null    str
#  10  subscribing_channel  1856 non-null   str
#  11  is_retained          1856 non-null   object
# dtypes: object(2), str(10)
# memory usage: 941.1+ KB

# sprawdzenie typu dla kolumny
# #  4   converted            10022 non-null  object
print(df['converted'].dtype)  # object

# zamienic na typ bool
df['converted'] = df['converted'].astype('bool')
print(df['converted'].dtype)  # bool
df.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 10037 entries, 0 to 10036
# Data columns (total 12 columns):
#  #   Column               Non-Null Count  Dtype
# ---  ------               --------------  -----
#  0   user_id              10037 non-null  str
#  1   date_served          10021 non-null  str
#  2   marketing_channel    10022 non-null  str
#  3   variant              10037 non-null  str
#  4   converted            10037 non-null  bool
#  5   language_displayed   10037 non-null  str
#  6   language_preferred   10037 non-null  str
#  7   age_group            10037 non-null  str
#  8   date_subscribed      1856 non-null   str
#  9   date_canceled        577 non-null    str
#  10  subscribing_channel  1856 non-null   str
#  11  is_retained          1856 non-null   object
# dtypes: bool(1), object(1), str(10)
# memory usage: 872.5+ KB
print(df.head(1).to_string())

# marketing_channel
# # House Ads
# is_house_ads -> True, False
df['is_house_ads'] = np.where(df['marketing_channel'] == "House Ads", True, False)
print(df.is_house_ads.head(3))
# 0    True
# 1    True
# 2    True
# Name: is_house_ads, dtype: bool
df.to_csv('marketing_is_house_ads.csv', sep=",", index=False)
