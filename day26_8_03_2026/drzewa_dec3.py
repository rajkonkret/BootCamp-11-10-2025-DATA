import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree

# pip install -U scikit-learn

# uczenie nadzorowane
#  zestaw danych posiada poprawne odpowiedzi
# [wiek, zarobki]
X = np.array(
    [
        [25, 30],
        [40, 70],
        [35, 50],
        [50, 90],
        [20, 20],
    ]
)

# etykiety (odpowiedzi) -> 1 tak, 0 nie
y = np.array([0, 1, 1, 1, 0])

# budowa i trenowanie drzewa decyzyjnego
tree = DecisionTreeClassifier(criterion='gini', max_depth=2)
tree.fit(X, y)  # trenowanie drzewa

# predykcja
decision = tree.predict(np.array([[30, 40]]))
print("Pożyczka przyznana" if decision[0] == 1 else "Pożyczka odrzucona")  # Pożyczka odrzucona

# wizualizacja drzewa
plt.figure(figsize=(8, 5))
plot_tree(tree, feature_names=['wiek', 'zarobki'],
          class_names=['odrzucona', 'przyznana'], filled=True)

plt.title("Drzewo decyzyjne: Przyznanie pożyczki")
plt.tight_layout()
plt.show()
