import matplotlib.pyplot as plt
import pandas as pd
from IPython.core.pylabtools import figsize
from sympy import rotations

df = pd.read_csv('marketing_ok_date.csv', sep=",")
print(df.head(3))

language_age = df.groupby(['language_preferred', 'age_group'])['user_id'].count()
language_age = pd.DataFrame(language_age.unstack(level=0))
print(language_age.head(10))

# language_age.plot(kind="bar")
#
# plt.title("Język w zależności od wieku")
# plt.xlabel("Wiek")
# plt.ylabel("Użytkownicy")
# plt.legend(loc="upper right", labels=language_age.columns.values)
# plt.xticks(rotation=45)
#
# plt.show()

language_age.plot(kind="line", figsize=(12, 7))

plt.title("Liczba użytkowników wg grupy wiekowej i preferowanego języka")
plt.xlabel("Grupa wiekowa")
plt.ylabel("Liczba użytkowników")
plt.xticks(rotation=45)
plt.legend(title="Język preferowany")

plt.tight_layout()

plt.show()
