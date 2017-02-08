import numpy as np

def is_sorted(arr):
    return all(a >= b for a, b in zip(arr[:-1], arr[1:]))

def get_fall_pos(arr: np.ndarray):
    fall, = np.where(arr[:-1] < arr[1:])
    return len(arr) - 1 if len(fall) == 0 else fall[0]

def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int):
    return (a * b) // gcd(a, b)

def reduce_fraction(a: int, b: int):
    d = gcd(a, b)
    return a // d, b // d