import pickle
import numpy as np


def adapt_array(array: np.ndarray) -> bytes:
    return pickle.dumps(
        (array.shape, array.dtype, array.tobytes())
        )


def convert_to_array(text: bytes) -> np.ndarray:
    shape, dtype, data = pickle.loads(text)
    return (np.frombuffer
            (data, dtype=dtype).reshape(shape)
            )


if __name__ == "__main__":
    array1: np.ndarray = np.array([[1, 2, 3], [1, 2, 3]])

    result: bytes = adapt_array(array1)
    print(result)
    print(convert_to_array(result))
