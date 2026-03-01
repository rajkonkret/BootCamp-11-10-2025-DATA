from typing import List, Tuple
import time
import random
import numpy as np

PythonArray2D = List[List[float]]


def multiply_python_arrays(x: PythonArray2D,
                           y: PythonArray2D) -> PythonArray2D:
    result = initialize_array_2D(
        shape=(len(x), len(y[0]))
    )

    for i in range(len(x)):
        for j in range(len(y[0])):
            dot_product = 0
            for k in range(len(x[0])):
                dot_product += x[i][k] * y[k][j]
            result[i][j] = dot_product
    return result


def initialize_array_2D(shape: Tuple[int, int]) -> PythonArray2D:
    return [
        [0.0 for _ in range(shape[1])]
        for _ in range(shape[0])
    ]


def generate_random_array2D(shape: Tuple[int, int]) -> PythonArray2D:
    result = initialize_array_2D(shape=shape)
    for row in range(shape[0]):
        for col in range(shape[1]):
            result[row][col] = random.random()
    return result
