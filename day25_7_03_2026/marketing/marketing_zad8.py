import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import function_tools

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

subscribes = email.groupby(['user_id', 'variant'])['converted'].max()
print(subscribes.head())
# user_id     variant
# a100000526  personalization     True
# a100000530  personalization     True
# a100000534  personalization    False
# a100000538  personalization     True
# a100000542  personalization     True
# Name: converted, dtype: bool

subscribers_df = pd.DataFrame(subscribes.unstack(level=1))
control = subscribers_df['control'].dropna()
print(control.head())
# user_id
# a100000687    False
# a100000688     True
# a100000689     True
# a100000690     True
# a100000691     True
# Name: control, dtype: object

control.info()
# <class 'pandas.Series'>
# Index: 270 entries, a100000687 to a100007293
# Series name: control
# Non-Null Count  Dtype
# --------------  -----
# 270 non-null    object
# dtypes: object(1)
# memory usage: 4.2+ KB

personalization = subscribers_df['personalization'].dropna()
print(personalization.tail())
# user_id
# a100007273    True
# a100007274    True

print("Control conversion rate:", np.mean(control))  # średnia
print("Personalization conversion rate:", np.mean(personalization))
# Control conversion rate: 0.2814814814814815, średnai
# Personalization conversion rate: 0.3908450704225352, średnai

print("Lift:", function_tools.lift(control, personalization))  # Lift: 39%

def ab_segmentation(segment):
    for subsegment in np.unique(df[segment].values):
        print(subsegment)

    email = df[(df["marketing_channel"] == 'Email') & (df[segment] == subsegment)]
    print(email.head().to_string())

    subscribers = email.groupby(['user_id', 'variant'])['converted'].max()
    print(subscribers.head())
    subscribers = pd.DataFrame(subscribers.unstack(level=1))

    control = subscribers['control'].dropna()
    personalization = subscribers['personalization'].dropna()
    print(control.dtype, personalization.dtype)

    print("lift:", function_tools.lift(control, personalization))
    control = control.astype(int)
    personalization = personalization.astype(int)
    print("T-satic:", stats.ttest_ind(control, personalization), '\n\n')  # t-static - różnica średnich
    # p < 0.05 może sugerowac powtarzalnośc wyników

ab_segmentation('language_displayed')
ab_segmentation('age_group')
# lift: -100%
# T-satic: TtestResult(statistic=np.float64(3.326565456420339), pvalue=np.float64(0.0016358623456360487), df=np.float64(51.0))