import os
import time
import numpy as np

# pip install tensorflow
# pip uninstall tensorflow

# pip install tensorflow-cpu
# pip install tensorflow-macos
# pip install tensorflow-metal (gpu)

# pip uninstall -y tensorflow tf-keras
# pip install "tensorflow<2.21,>=2.20" "tf-keras==2.20.1"
# python -c "import platform; print(platform.machine())"
import tensorflow as tf
from tensorflow import keras
from keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("Dostępne urządzenia")
print(tf.config.list_physical_devices())  # [PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]
print("Czy GPU jest dostępne:", tf.config.list_physical_devices('GPU'))  # Czy GPU jest dostępne: []

# dane wejściowe
X = np.array(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
)

# dane do nauki
y_xor = np.array([[0], [1], [1], [0]])
y_and = np.array([[0], [0], [0], [1]])
y_or = np.array([[0], [1], [1], [1]])


def train_model(y_train, logic_type):
    print(f"Uczenie modelu dla operacji: {logic_type}")

    # definiujemy model
    model = Sequential(
        [
            Input(shape=(2,)),
            Dense(4, activation="relu"),  # warstwa ukryta, 4 neurony, funkcja relu
            Dense(1, activation="sigmoid")  # warstwa wyjsciowa, sigmoid
        ]
    )

    # kompilacja modelu
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])

    # uruchomienie nauki
    with tf.device("/GPU:0"):
        model.fit(X, y_train, epochs=100, verbose=1)

    # testowanie modelu
    predictions = model.predict(X)
    predictions = (predictions > 0.5).astype(int)

    print(f"Przewidywanie wyników dla operacji {logic_type}")
    for i in range(len(X)):
        print(f"{X[i]} {predictions[i][0]} oczekiwanie: {y_train[i][0]}")

    return model


start_time = time.time()

model_and = train_model(y_and, "AND")

print(f"Estimated time: {time.time() - start_time}")
