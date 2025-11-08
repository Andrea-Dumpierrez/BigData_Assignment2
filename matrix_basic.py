import numpy as np

def multiply_basic(A, B):
    """
    Basic matrix multiplication using NumPy's dot operator.
    A and B must be square matrices of the same size.
    """
    return A @ B  # Standard O(n^3) matrix multiplication
