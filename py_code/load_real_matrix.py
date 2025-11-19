import numpy as np
from scipy.io import mmread

# Load the real sparse matrix
matrix = mmread("mc2depi.mtx")

print("=== MATRIX INFO ===")
print("Type:", type(matrix))
print("Shape:", matrix.shape)
print("Non-zero values (nnz):", matrix.nnz)
print("Sparsity (%):", 100 * (1 - matrix.nnz / (matrix.shape[0] * matrix.shape[1])))
