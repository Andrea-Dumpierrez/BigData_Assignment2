import numpy as np
from scipy import sparse

def multiply_sparse(A, B, sparsity=0.8):
    """
    Sparse matrix multiplication using SciPy.
    A and B are dense NumPy matrices.
    'sparsity' defines the fraction of zero elements to insert (0–1).
    """
    # Copy to avoid modifying the original matrices
    M = A.copy()
    N = B.copy()

    # Create random masks: True means the value will be set to zero
    maskA = np.random.rand(*A.shape) < sparsity
    maskB = np.random.rand(*B.shape) < sparsity

    M[maskA] = 0
    N[maskB] = 0

    # Convert dense arrays to sparse CSR format
    A_sparse = sparse.csr_matrix(M)
    B_sparse = sparse.csr_matrix(N)

    # Multiply sparse matrices
    C_sparse = A_sparse.dot(B_sparse)

    return C_sparse
