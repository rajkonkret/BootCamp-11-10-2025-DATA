import pandas as pd
from torch.ao.quantization import prepare_qat

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

lang_conv = fun.conversion_rate(house_ads_b, ['language_displayed'])
print("lang_conv:", lang_conv)
# lang_conv: language_displayed
# Arabic     1.000000
# English    0.865854
# German     0.857143
# Spanish    0.894737
# Name: user_id, dtype: float64

spanish_index = lang_conv['Spanish'] / lang_conv['English']
arabic_index = lang_conv['Arabic'] / lang_conv['English']
german_index = lang_conv['German'] / lang_conv['English']

print("Spanish index:", spanish_index)
print("Arabic index:", arabic_index)
print("German index:", german_index)
# Spanish index: 1.033358042994811
# Arabic index: 1.1549295774647887
# German index: 0.9899396378269617

converted = (house_ads.groupby(['date_served', 'language_preferred'])
             .agg({"user_id": "nunique", "converted": "sum"}))
print(converted.head(3))
#                                 user_id  converted
# date_served language_preferred
# 2018-01-01  Arabic                    2          2
#             English                  29         13
#             German                    2          1

converted = pd.DataFrame(converted.unstack(level=1))
print(converted.head(3))
# language_preferred  Arabic English German  ...   English German Spanish
# date_served                                ...
# 2018-01-01             2.0    29.0    2.0  ...      13.0    1.0     NaN
# 2018-01-02             NaN    14.0    3.0  ...      14.0    3.0     NaN
# 2018-01-03             NaN    15.0    1.0  ...      15.0    1.0     1.0

print(45 * "-")
converted['english_conv_rate'] = (converted.loc['2018-01-11':'2018-01-31'][('converted', 'English')] /
                                  converted.loc['2018-01-11':'2018-01-31'][('user_id', 'English')])

# print(converted.head(3))
print(converted.tail())
#                    user_id                 ... converted         english_conv_rate
# language_preferred  Arabic English German  ...    German Spanish
# date_served                                ...
# 2018-01-27             1.0     4.0    NaN  ...       NaN     1.0               1.0
# 2018-01-28             NaN     4.0    NaN  ...       NaN     2.0               1.0
# 2018-01-29             2.0     3.0    NaN  ...       NaN     NaN               1.0
# 2018-01-30             NaN     4.0    NaN  ...       NaN     2.0               1.0
# 2018-01-31             1.0     4.0    NaN  ...       NaN     1.0               1.0

converted['expected_spanish_rate'] = converted['english_conv_rate'] * spanish_index
converted['expected_arabic_rate'] = converted['english_conv_rate'] * arabic_index
converted['expected_german_rate'] = converted['english_conv_rate'] * german_index

print(converted['expected_spanish_rate'])  # 2018-01-11    1.033358

converted['expected_spanish_conv'] = converted['expected_spanish_rate'] * converted[('user_id', 'Spanish')]
converted['expected_arabic_conv'] = converted['expected_arabic_rate'] * converted[('user_id', 'Arabic')]
converted['expected_german_conv'] = converted['expected_german_rate'] * converted[('user_id', 'German')]

print(converted['expected_spanish_conv'])  # 2018-01-12    1.033358

converted = converted.loc['2018-01-11':'2018-01-31']

expected_subs = (
        converted['expected_spanish_conv'].sum()
        + converted['expected_arabic_conv'].sum()
        + converted['expected_german_conv'].sum()
)

print("Expected:", expected_subs)  # Expected: 27.457799428147837

# actual_subs = (
#         converted[('converted', 'Spanish')].sum()
#         + converted[('converted', 'Arabic')].sum()
#         + converted[('converted', 'German')].sum()
# )

# bardziej pythonicznie
actual_subs = sum([
    converted[('converted', 'Spanish')].sum(),
    converted[('converted', 'Arabic')].sum(),
    converted[('converted', 'German')].sum(),
])
print("Actual subs:", actual_subs)  # Actual subs: 26.0
