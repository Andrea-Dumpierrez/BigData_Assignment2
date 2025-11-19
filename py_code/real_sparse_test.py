import time
from scipy.io import mmread
from scipy.sparse import csr_matrix

# Load matrix
A = mmread("mc2depi.mtx").tocsr()

print("Matrix loaded.")
print("Shape:", A.shape)
print("NNZ:", A.nnz)

# Multiplying sparse matrix by a random sparse vector (REALISTIC TEST)
import numpy as np
x = np.random.rand(A.shape[1])

start = time.perf_counter()
y = A.dot(x)
end = time.perf_counter()

print("\n=== REAL SPARSE MATRIX TEST ===")
print("Time (A * x):", round(end - start, 6), "seconds")
print("Output vector shape:", y.shape)
