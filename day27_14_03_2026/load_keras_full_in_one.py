import numpy as np

# wczytanie modelu
loaded_weights = np.load("weights_only_full.npz")

print('Dostępne parametry')
print(loaded_weights.files)
# Dostępne parametry
# ['arr_0', 'arr_1', 'arr_2', 'arr_3']

param_name = loaded_weights.files[0]
param_array = loaded_weights[param_name]

print(f"Parametr: {param_name}")  # Parametr: arr_0
print(f"Kształt: {param_array.shape}")  # Kształt: (2, 4)
print(f"Dane: {param_array.flatten()[:5]}")
# Dane: [-1.5407417  0.7708068  1.7060478  1.0624772  0.8778308]

# z = X * W + b
W_input_hidden = loaded_weights['arr_0']  # wagi - warstwa ukryta - wejście
b_hidden = loaded_weights['arr_1']  # bias warstwy ukrytej
W_hidden_output = loaded_weights['arr_2']  # wyjśćie warstwy ukrytej
b_output = loaded_weights['arr_3']  # bias wyjścia

# dane wejściowe
X = np.array(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
)

y_expected = np.array(
    [
        [0, 0, 0],  # and, or, xor
        [0, 1, 1],
        [0, 1, 1],
        [1, 1, 0],
    ]
)
