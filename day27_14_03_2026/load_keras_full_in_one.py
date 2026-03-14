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

def relu(x):
    return np.maximum(0, x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# warstwa ukryta
hidden_layer = np.dot(X, W_input_hidden) + b_hidden
hidden_layer = relu(hidden_layer)

# warstwa wyjściowa
predictions = np.dot(hidden_layer, W_hidden_output) + b_output
predictions = sigmoid(predictions)

print('Predictions shape:', predictions.shape)

predictions = (predictions > 0.5).astype(int)

# sprawdzanie wyników odpowiedzi
y_expected = np.array(
    [
        [0, 0, 0],  # and, or, xor
        [0, 1, 1],
        [0, 1, 1],
        [1, 1, 0],
    ]
)

print("Przewidywane wartości dla AND, OR, XOR\n")
for i in range(len(X)):
    print(f"Wejście {X[i]} => AND: {predictions[i][0]} OR: {predictions[i][1]}, XOR: {predictions[i][2]}")

