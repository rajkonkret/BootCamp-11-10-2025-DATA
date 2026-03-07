import numpy as np
import pandas as pd

# df = pd.read_csv('marketing_r.csv')
# print(df.head().to_string())

df = pd.read_csv('marketing_r.csv', sep=",")
print(df.head(1).to_string())

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
# print(df.is_house_ads.head(3))
# 0    True
# 1    True
# 2    True
# Name: is_house_ads, dtype: bool
df.to_csv('marketing_is_house_ads.csv', sep=",", index=False)

# zamiana dat na fdatetime
df['date_served'] = pd.to_datetime(df['date_served'], errors='coerce', format='mixed')
# print(df['date_served'].head(3))

channel_dict = {"House Ads": 1, "Instagram": 2, "Facebook": 3, "Email": 4, 'Push': 5}
df['channel_code'] = df['marketing_channel'].map(channel_dict)

# unikalni użytkownicy dziennie
daily_users = df.groupby(['date_served'])['user_id'].nunique()
print("Dziennie:", daily_users)

df.to_csv("marketing_ok_date.csv")

subscribers = df[df['converted'] == True]['user_id'].nunique()
total = df['user_id'].nunique()
print("Subscribers:", subscribers)
print("Total:", total)
# Subscribers: 1030
# Total: 7309

# współczynnik konwersji
conv_rate = subscribers / total
print("Covert rate:", conv_rate)  # Covert rate: 0.14092215077301956
# Covert rate: 14.09 %
print("Covert rate:", round(conv_rate * 100, 2), "%")  # Covert rate: 14.09 %

# współczynnik utrzymania użytkowników
# retained -> is_retained
retained = df[df['is_retained'] == True]['user_id'].nunique()
retention = retained / subscribers
print("Retention rate:", round(retention * 100, 2), "%")
print("Retention rate:", round(retention * 100, 2), "%")  # Retention rate: 65.83 %

# House Ads
house_ads = df[df['subscribing_channel'] == "House Ads"]
retained = house_ads[house_ads['is_retained'] == True]['user_id'].nunique()
subscribers = house_ads[house_ads['converted'] == True]['user_id'].nunique()
retention_rate = retained / subscribers
print("Retention rate:", round(retention_rate * 100, 2), "%")  # Retention rate: 16.8 %
# Retention rate: 58.05 %

retained = df[df['is_retained'] == True].groupby(['subscribing_channel'])['user_id'].nunique()
print(retained)
# subscribing_channel
# Email        141
# Facebook     152
# House Ads    173
# Instagram    158
# Push          54
# Name: user_id, dtype: int64

subscribers = df[df['converted'] == True].groupby(['subscribing_channel'])['user_id'].nunique()
print(subscribers)
# subscribing_channel
# Email        161
# Facebook     221
# House Ads    298
# Instagram    232
# Push          77
# Name: user_id, dtype: int64

channel_retension_rate = (retained / subscribers) * 100
print(channel_retension_rate)
# subscribing_channel
# Email        87.577640
# Facebook     68.778281
# House Ads    58.053691
# Instagram    68.103448
# Push         70.129870
# Name: user_id, dtype: float64

import matplotlib.pyplot as plt

# bar
channel_retension_rate.plot(kind='bar')

plt.title("Wskażnik utrzymania wg kanału")
plt.xlabel("Kanał", size=14)
plt.ylabel("Konwersja (%)", size=14)
plt.xticks(rotation=45)

plt.show()
