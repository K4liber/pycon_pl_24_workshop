import numpy as np


def test_numpy(n: int = 34) -> np.array:
    """
    Dumb calculations on numpy arrays.
    """

    for _ in range(100000):
        np.array([1, 2, 3]) * n

    return np.array([1, 2, 3]) * n
