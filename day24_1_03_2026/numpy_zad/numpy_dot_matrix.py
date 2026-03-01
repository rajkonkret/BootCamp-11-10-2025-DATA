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


if __name__ == '__main__':
    # macierze pythonowe
    PYTHON_ARRAY_A = generate_random_array2D(shape=(500, 500))
    PYTHON_ARRAY_B = generate_random_array2D(shape=(500, 500))

    # macierze numpy
    NUMPY_ARRAY_A = np.array(PYTHON_ARRAY_A)
    NUMPY_ARRAY_B = np.array(PYTHON_ARRAY_B)

    start_time = time.time()
    python_operation_result = multiply_python_arrays(x=PYTHON_ARRAY_A, y=PYTHON_ARRAY_B)
    python_exec_time = time.time() - start_time
    print(f"Pure Python time: {python_exec_time}")
    print(python_operation_result[10][10])

    start_time = time.time()
    numpy_operation_result = NUMPY_ARRAY_A.dot(NUMPY_ARRAY_B)  # mnożenie macierzy
    numpy_exec_time = time.time() - start_time
    print(f"Numpy time: {numpy_exec_time}")
    print(numpy_operation_result[10, 10])

    print("Ratio:", python_exec_time / numpy_exec_time)

    result_diff = np.sum(np.absolute(numpy_operation_result - np.array(python_operation_result)))
    print(result_diff)  # 1.6583641126999282e-09
    print(result_diff < 1e-5)  # True
# Pure Python time: 11.850436925888062
# 133.8914057103311
# Numpy time: 0.002416849136352539
# 133.8914057103311
# Ratio: 4903.258853704252
# 1.6527366142327082e-09
# True
