import numpy as np
from typing import Tuple, List


def _euclidean_distance(array1: np.ndarray, array2: np.ndarray) -> np.floating:
    """
    Calculate the Euclidean distance between two points represented as NumPy arrays.
    """
    if array1.shape != array2.shape:
        raise ValueError("Input points must have the same shape.")

    # Calculate the Euclidean distance
    distance: np.floating = np.linalg.norm(array1 - array2)

    return distance


def get_nearest_neighbor(train: List[np.ndarray],
                         test_row: np.ndarray,
                         num_neighbors: int = 1):
    """
    Find the nearest neighbors of a test data point in a dataset.
    """
    if num_neighbors <= 0:
        raise ValueError("")

    if num_neighbors > len(train):
        raise ValueError("")

    distances: list = []

    for train_row in train:
        dist: np.floating = _euclidean_distance(test_row, train_row)
        distances.append([train_row, dist])

    distances.sort(key=lambda tup: tup[1])
    neighbors: list = []

    for i in range(num_neighbors):
        neighbors.append(distances[i])

    return neighbors
