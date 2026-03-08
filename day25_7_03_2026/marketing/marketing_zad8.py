import matplotlib.pyplot as plt
import pandas as pd
import marketing_zad6 as fun

# df = pd.read_csv('marketing_ok_date.csv', sep=",")
df = pd.read_csv('marketing_is_house_ads.csv', sep=",")
print(df.head(3))

print(df['date_served'].dtype)  # str
df['date_served'] = pd.to_datetime(df['date_served'], format="%m/%d/%y")
print(df.head(3))
#       user_id date_served  ... is_retained is_house_ads
# 0  a100000029  2018-01-01  ...        True         True

email = df[df['marketing_channel'] == 'Email']
print(email.head().to_string())

# upenienie się, ze grupy zostały odpowiednio zbalnasowane
alloc = email.groupby(['variant'])['user_id'].nunique()
print(alloc.head())
# variant
# control            270
# personalization    284
# Name: user_id, dtype: int64

# alloc.plot(kind="bar")
# plt.title("Personalizacja testu")
# plt.ylabel("Liczba")
# plt.show()
