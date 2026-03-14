import os
import numpy as np

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # przed importowaniem kerasa

import tensorflow as tf
from tensorflow import keras
from keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

X = []
y = []
