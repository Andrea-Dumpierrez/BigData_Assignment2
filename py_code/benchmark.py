import time
import numpy as np
from memory_profiler import memory_usage

from matrix_basic import multiply_basic
from matrix_strassen import strassen
from matrix_block import multiply_block
from matrix_sparse import multiply_sparse


def measure_time_and_memory(func, *args, **kwargs):
    """
    Measure execution time and memory usage for a given function.
    Returns: result, elapsed_time, memory_used
    """
    start_time = time.time()
    mem_before = memory_usage()[0]
    result = func(*args, **kwargs)
    mem_after = memory_usage()[0]
    elapsed_time = time.time() - start_time
    memory_used = mem_after - mem_before
    return result, elapsed_time, memory_used


def benchmark_matrix_sizes(sizes, sparsity_levels):
    """
    Run benchmarks for different matrix sizes and sparsity levels.
    Prints time and memory usage for each method.
    """
    for n in sizes:
        print(f"\n=== Matrix size: {n}x{n} ===")
        A = np.random.rand(n, n)
        B = np.random.rand(n, n)

        # Basic
        _, t_basic, m_basic = measure_time_and_memory(multiply_basic, A, B)
        print(f"Basic: {t_basic:.4f}s, Memory: {m_basic:.2f} MiB")

        # Strassen
        if n & (n - 1) == 0:  # Strassen works best for powers of two
            _, t_strassen, m_strassen = measure_time_and_memory(strassen, A, B)
            print(f"Strassen: {t_strassen:.4f}s, Memory: {m_strassen:.2f} MiB")
        else:
            print("Strassen: skipped (size not power of 2)")

        # Block
        _, t_block, m_block = measure_time_and_memory(multiply_block, A, B)
        print(f"Block: {t_block:.4f}s, Memory: {m_block:.2f} MiB")

        # Sparse (test each sparsity level)
        for s in sparsity_levels:
            _, t_sparse, m_sparse = measure_time_and_memory(multiply_sparse, A, B, s)
            print(f"Sparse ({int(s*100)}% zeros): {t_sparse:.4f}s, Memory: {m_sparse:.2f} MiB")


if __name__ == "__main__":
    sizes = [64, 128, 256]  # You can add 512, 1024 later if your PC allows it
    sparsity_levels = [0.25, 0.5, 0.75]
    benchmark_matrix_sizes(sizes, sparsity_levels)
