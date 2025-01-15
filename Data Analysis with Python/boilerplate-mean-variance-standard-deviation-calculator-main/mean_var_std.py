import numpy as np


def calculate(lst):

    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(lst).reshape(3, 3)

    functions = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum,
    }
    calculations = {}
    for func_name, func in functions.items():
        calculations[func_name] = [
            func(array, axis=0).tolist(),
            func(array, axis=1).tolist(),
            func(array),
        ]

    return calculations
