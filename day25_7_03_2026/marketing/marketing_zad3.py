import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('marketing_ok_date.csv', sep=",")
print(df.head(3))

#
language = df.groupby(['date_served', 'language_preferred'])['user_id'].count()
print(language.head(10))
# date_served  language_preferred
# 2018-01-01   Arabic                  4
#              English               355
#              German                  5
#              Spanish                11
# 2018-01-02   Arabic                  4
#              English               397
#              German                  6
#              Spanish                10
# 2018-01-03   Arabic                  3
#              English               374

# zamiana kolumn z wierszami
language = pd.DataFrame(language.unstack(level=1))
print(language)
# language_preferred  Arabic  English  German  Spanish
# date_served
# 2018-01-01             4.0    355.0     5.0     11.0
# 2018-01-02             4.0    397.0     6.0     10.0
# 2018-01-03             3.0    374.0     3.0      8.0
# 2018-01-04             2.0    318.0     2.0     14.0

# level - wskazuje kolumnę, która ma być nagłówkiem
# language = pd.DataFrame(language.unstack(level=0))
# print(language.head())

# date_served         2018-01-01  2018-01-02  ...  2018-01-30  2018-01-31
# language_preferred                          ...
# Arabic                     4.0         4.0  ...         6.0         8.0

language.plot()

plt.title("Dzienne preferencje językowe")
plt.xlabel("Data")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper right", labels=language.columns.values)
plt.xticks(rotation=45)

plt.show()

language = df.groupby(['date_served', 'language_preferred'])['user_id'].count()
language = pd.DataFrame(language.unstack(level=0))
print(language.head())

language.plot()
plt.title("Dzienne preferencje językowe")
plt.xlabel("Data")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper right", labels=language.columns.values)
plt.xticks(rotation=45)

plt.show()
