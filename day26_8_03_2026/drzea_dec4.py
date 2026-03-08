import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn import metrics

dane = [
    {"wiek": 55, "zarobki": 70, "decyzja": "tak"},  # 1
    {"wiek": 53, "zarobki": 50, "decyzja": "nie"},  # 0
    {"wiek": 47, "zarobki": 60, "decyzja": "tak"},  # 1
    {"wiek": 40, "zarobki": 30, "decyzja": "nie"},  # 0
    {"wiek": 35, "zarobki": 45, "decyzja": "tak"},  # 1
    {"wiek": 28, "zarobki": 65, "decyzja": "nie"},  # 0
    {"wiek": 31, "zarobki": 42, "decyzja": "tak"},  # 1
    {"wiek": 29, "zarobki": 50, "decyzja": "nie"},  # 0
    {"wiek": 52, "zarobki": 80, "decyzja": "tak"},  # 1
    {"wiek": 60, "zarobki": 55, "decyzja": "tak"},  # 1
]

# [1 0 1 0 1 0 1 0 1 1]
df = pd.DataFrame(dane)
df['decyzja_bin'] = df['decyzja'].map({'nie': 0, "tak": 1})
print(df.head())
#    wiek  zarobki decyzja  decyzja_bin
# 0    55       70     tak            1
# 1    53       50     nie            0
# 2    47       60     tak            1
# 3    40       30     nie            0
# 4    35       45     tak            1
print(df['decyzja_bin'])

X = df[['wiek', 'zarobki']]
y = df['decyzja_bin']

model = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
model.fit(X, y)

y_pred = model.predict(X)  # model odpowiada
print(y_pred)

test_input = pd.DataFrame([
    {"wiek": 34, "zarobki": 60},
    {"wiek": 50, "zarobki": 40},
    {"wiek": 28, "zarobki": 30},
    {"wiek": 45, "zarobki": 65},
    {"wiek": 37, "zarobki": 35},
    {"wiek": 60, "zarobki": 20}
])
