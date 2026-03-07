import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('marketing_ok_date.csv', sep=",")

retention_total = df['user_id'].nunique()
print(retention_total)  # 7309

retention_total = df.groupby(['date_subscribed', 'subscribing_channel'])['user_id'].nunique()
print(retention_total.head(3))
# date_subscribed  subscribing_channel
# 1/1/18           Email                   1
#                  Facebook                8
#                  House Ads              16
# Name: user_id, dtype: int64

retention_subs = df[df['is_retained'] == True].groupby(['date_subscribed', 'subscribing_channel'])['user_id'].nunique()
print(retention_subs)
# date_subscribed  subscribing_channel
# 1/1/18           Email                   1
#                  Facebook                7
#                  House Ads              11
#                  Instagram               6
#                  Push                    3

retention_rate = retention_subs / retention_total
print(retention_rate.head(3))
# date_subscribed  subscribing_channel
# 1/1/18           Email                  1.0000
#                  Facebook               0.8750
#                  House Ads              0.6875
# Name: user_id, dtype: float64

retention_rate = pd.DataFrame(retention_rate.unstack(level=1))
print(retention_rate.tail())  # pięć ostatnich
# subscribing_channel  Email  Facebook  House Ads  Instagram      Push
# date_subscribed
# 1/5/18                 1.0  0.571429   0.500000   0.636364  1.000000
# 1/6/18                 0.8  0.571429   0.941176   0.500000  0.500000
# 1/7/18                 0.5  0.750000   0.526316   0.400000  0.666667
# 1/8/18                 NaN  0.888889   0.500000   0.625000  1.000000
# 1/9/18                 0.5  0.285714   0.850000   0.666667  0.500000
