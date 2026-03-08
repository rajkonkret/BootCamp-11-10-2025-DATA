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

house_ads = df[df['subscribing_channel'] == "House Ads"]
print(house_ads.head(3))

house_ads_b = house_ads[house_ads['date_served'] < '2018-01-11']
print(house_ads_b)
