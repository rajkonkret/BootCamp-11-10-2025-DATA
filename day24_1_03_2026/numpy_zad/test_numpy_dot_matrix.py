# wygenerowane za pomocą copilot

import unittest
import numpy as np
import random
import time

from .numpy_dot_matrix import (
    multiply_python_arrays,
    initialize_array_2D,
    generate_random_array2D,
)


class TestMatrixMultiplication(unittest.TestCase):

    def test_initialize_array(self):
        arr = initialize_array_2D((3, 4))
        self.assertEqual(len(arr), 3)
        self.assertEqual(len(arr[0]), 4)
        self.assertTrue(all(all(v == 0.0 for v in row) for row in arr))

    def test_small_matrix_multiplication(self):
        x = [
            [1, 2],
            [3, 4]
        ]
        y = [
            [5, 6],
            [7, 8]
        ]

        expected = np.array(x).dot(np.array(y))
        result = multiply_python_arrays(x, y)

        np.testing.assert_allclose(result, expected, rtol=1e-7, atol=1e-7)

    def test_random_matrix_multiplication(self):
        random.seed(0)
        np.random.seed(0)

        x = generate_random_array2D((5, 5))
        y = generate_random_array2D((5, 5))

        expected = np.array(x).dot(np.array(y))
        result = multiply_python_arrays(x, y)

        np.testing.assert_allclose(result, expected, rtol=1e-7, atol=1e-7)

    def test_non_square_matrices(self):
        x = generate_random_array2D((4, 3))  # 4x3
        y = generate_random_array2D((3, 2))  # 3x2

        expected = np.array(x).dot(np.array(y))
        result = multiply_python_arrays(x, y)

        np.testing.assert_allclose(result, expected, rtol=1e-7, atol=1e-7)

    # nasza funkcja nie ma tej funkcjonalności
    # def test_dimension_mismatch(self):
    #     x = generate_random_array2D((3, 4))
    #     y = generate_random_array2D((5, 6))
    #
    #     with self.assertRaises(IndexError):
    #         multiply_python_arrays(x, y)

    def test_performance_small(self):
        x = generate_random_array2D((50, 50))
        y = generate_random_array2D((50, 50))

        start = time.time()
        multiply_python_arrays(x, y)
        duration = time.time() - start

        self.assertLess(duration, 1.0)  # powinno się zmieścić w 1 sekundzie

    def test_compare_with_numpy_large(self):
        x = generate_random_array2D((100, 100))
        y = generate_random_array2D((100, 100))

        expected = np.array(x).dot(np.array(y))
        result = multiply_python_arrays(x, y)

        diff = np.sum(np.abs(expected - np.array(result)))
        self.assertLess(diff, 1e-5)


if __name__ == "__main__":
    unittest.main()
