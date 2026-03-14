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
print(tf.config.list_physical_devices()) # [PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]
print("Czy GPU jest dostępne:", tf.config.list_physical_devices('GPU')) # Czy GPU jest dostępne: []