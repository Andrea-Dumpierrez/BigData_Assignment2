import numpy as np

def multiply_block(A, B, block_size=64):
    """
    Blocked (cache-friendly) matrix multiplication.
    Splits A and B into sub-blocks to improve cache locality.
    Works for any square size n (not necessarily a multiple of block_size).
    """
    n = A.shape[0]
    C = np.zeros((n, n), dtype=A.dtype)

    for i in range(0, n, block_size):
        i_end = min(i + block_size, n)
        for k in range(0, n, block_size):
            k_end = min(k + block_size, n)
            # Preload the A sub-block to reduce repeated slicing
            A_block = A[i:i_end, k:k_end]
            for j in range(0, n, block_size):
                j_end = min(j + block_size, n)
                # Multiply sub-blocks and accumulate
                C[i:i_end, j:j_end] += A_block @ B[k:k_end, j:j_end]
    return C
