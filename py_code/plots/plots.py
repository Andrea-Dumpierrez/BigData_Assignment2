import matplotlib.pyplot as plt
import os

# Ensure plots directory exists
os.makedirs("plots", exist_ok=True)

sizes = [64, 128, 256]

# Python times
py_basic=[0.2007,0.2018,0.2033]
py_strassen=[0.2006,0.2027,0.2053]
py_block=[0.2006,0.2031,0.2040]
py_sparse25=[0.2056,0.2075,0.2288]
py_sparse50=[0.2016,0.2052,0.2188]
py_sparse75=[0.2022,0.2053,0.2118]

# Python memory
py_mem_basic=[0.08,0.45,0.94]
py_mem_strassen=[0.03,0.44,0.59]
py_mem_block=[0.04,0.03,0.59]
py_mem_sparse25=[0.27,0.23,0.77]
py_mem_sparse50=[0.09,0.03,0.88]
py_mem_sparse75=[0.00,0.00,0.27]

# Java
java_basic=[2,2,18]
java_block=[3,2,12]
java_strassen=[3,6,18]

# C
c_basic=[0.0008,0.0030,0.0580]
c_block=[0.0000,0.0000,0.0540]
c_strassen=[0.0610,0.4320,2.7080]

# --- Python time plot ---
plt.figure()
plt.plot(sizes,py_basic,label="Basic")
plt.plot(sizes,py_strassen,label="Strassen")
plt.plot(sizes,py_block,label="Block")
plt.plot(sizes,py_sparse25,label="Sparse 25%")
plt.plot(sizes,py_sparse50,label="Sparse 50%")
plt.plot(sizes,py_sparse75,label="Sparse 75%")
plt.xlabel("Matrix Size")
plt.ylabel("Time (s)")
plt.title("Python Execution Time")
plt.legend()
plt.savefig("plots/python_time.png")
plt.close()

# --- Python memory plot ---
plt.figure()
plt.plot(sizes,py_mem_basic,label="Basic")
plt.plot(sizes,py_mem_strassen,label="Strassen")
plt.plot(sizes,py_mem_block,label="Block")
plt.plot(sizes,py_mem_sparse25,label="Sparse 25%")
plt.plot(sizes,py_mem_sparse50,label="Sparse 50%")
plt.plot(sizes,py_mem_sparse75,label="Sparse 75%")
plt.xlabel("Matrix Size")
plt.ylabel("Memory (MiB)")
plt.title("Python Memory Usage")
plt.legend()
plt.savefig("plots/python_memory.png")
plt.close()

# --- Java time plot ---
plt.figure()
plt.plot(sizes,java_basic,label="Basic")
plt.plot(sizes,java_block,label="Block")
plt.plot(sizes,java_strassen,label="Strassen")
plt.xlabel("Matrix Size")
plt.ylabel("Time (ms)")
plt.title("Java Execution Time")
plt.legend()
plt.savefig("plots/java_time.png")
plt.close()

# --- C time plot ---
plt.figure()
plt.plot(sizes,c_basic,label="Basic")
plt.plot(sizes,c_block,label="Block")
plt.plot(sizes,c_strassen,label="Strassen")
plt.xlabel("Matrix Size")
plt.ylabel("Time (s)")
plt.title("C Execution Time")
plt.legend()
plt.savefig("plots/c_time.png")
plt.close()

# --- Cross-language basic comparison ---
plt.figure()
plt.plot(sizes,py_basic,label="Python Basic")
plt.plot(sizes,java_basic,label="Java Basic")
plt.plot(sizes,c_basic,label="C Basic")
plt.xlabel("Matrix Size")
plt.ylabel("Time")
plt.title("Basic Comparison Across Languages")
plt.legend()
plt.savefig("plots/basic_compare.png")
plt.close()

print("All plots generated successfully!")
