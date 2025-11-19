import numpy as np
from matrix_basic import multiply_basic
from matrix_strassen import strassen
# from matrix_block import multiply_block  # Uncomment later when implemented

# Test Basic Multiplication
print("=== Testing Basic Matrix Multiplication ===")
A = np.random.randint(0, 10, (3, 3))
B = np.random.randint(0, 10, (3, 3))

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Result (Basic):\n", multiply_basic(A, B))

# Test Strassen Algorithm
print("\n=== Testing Strassen Algorithm ===")
A = np.random.randint(0, 10, (8, 8))
B = np.random.randint(0, 10, (8, 8))
print("Strassen result is correct:", np.allclose(strassen(A, B), A @ B))


from matrix_block import multiply_block

print("\n=== Testing Block Matrix Multiplication ===")
A = np.random.randint(0, 10, (8, 8))
B = np.random.randint(0, 10, (8, 8))
print("Block result is correct:", np.allclose(multiply_block(A, B), A @ B))



from matrix_sparse import multiply_sparse

print("\n=== Testing Sparse Matrix Multiplication ===")
A = np.random.rand(6, 6)
B = np.random.rand(6, 6)

for level in [0.25, 0.5, 0.75]:
    C_sparse = multiply_sparse(A, B, sparsity=level)
    print(f"Sparsity {level*100:.0f}% → Non-zeros in result:", C_sparse.nnz)
