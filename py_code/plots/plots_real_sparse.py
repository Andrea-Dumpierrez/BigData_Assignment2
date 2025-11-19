import time
import numpy as np
from scipy.io import mmread
import matplotlib.pyplot as plt

# 1. Cargar la matriz real (ruta relativa desde py_code)
print("Loading real sparse matrix...")
A = mmread("../mc2depi.mtx").tocsr()
n_rows, n_cols = A.shape
print(f"Shape: {A.shape}")

# 2. Crear un vector x aleatorio para el producto A * x
x = np.random.rand(n_cols)

# 3. Ejecutar varias veces A * x y medir tiempos
n_runs = 5          # número de repeticiones
times = []

for i in range(n_runs):
    start = time.time()
    y = A.dot(x)
    end = time.time()
    elapsed = end - start
    times.append(elapsed)
    print(f"Run {i+1}: {elapsed:.5f} s")

avg_time = sum(times) / len(times)
print(f"\nAverage time: {avg_time:.5f} s")

# 4. Hacer la gráfica
runs = list(range(1, n_runs + 1))

plt.figure(figsize=(8, 5))
plt.plot(runs, times, marker="o")
plt.axhline(avg_time, linestyle="--", label=f"Average = {avg_time:.5f} s")

plt.xlabel("Run")
plt.ylabel("Time (seconds)")
plt.title("SpMV (A · x) with real sparse matrix mc2depi")
plt.legend()
plt.grid(True)

# 5. Guardar la figura como imagen para la memoria
plt.tight_layout()
plt.savefig("real_sparse_spmv.png", dpi=300)
plt.show()
