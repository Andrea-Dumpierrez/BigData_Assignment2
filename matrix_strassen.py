import numpy as np

def strassen(A, B):
    """
    Strassen's algorithm for square matrix multiplication.
    Reduces the number of multiplications from 8 to 7 per recursive step.
    """
    assert A.shape == B.shape, "Matrices must be square and of the same size"
    n = A.shape[0]

    # Base case: use standard multiplication for small matrices
    if n <= 64:
        return A @ B

    # Split matrices into four submatrices
    k = n // 2
    A11, A12, A21, A22 = A[:k, :k], A[:k, k:], A[k:, :k], A[k:, k:]
    B11, B12, B21, B22 = B[:k, :k], B[:k, k:], B[k:, :k], B[k:, k:]

    # Compute the seven Strassen products
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # Combine results into the final matrix
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Join submatrices
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))
