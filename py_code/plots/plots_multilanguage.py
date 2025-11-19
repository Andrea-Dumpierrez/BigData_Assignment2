import matplotlib.pyplot as plt
import numpy as np

# ================================
# DATA (your real results)
# ================================
sizes = [64, 128, 256]

# Python (ms)
py_basic = [0.2007, 0.2018, 0.2033]
py_block = [0.2006, 0.2031, 0.2040]
py_strassen = [0.2006, 0.2027, 0.2053]

# Java (ms)
java_basic = [2, 2, 18]
java_block = [3, 2, 12]
java_strassen = [3, 6, 18]

# C (ms)
c_basic = [0.8, 3.0, 58.0]
c_block = [0.0, 0.0, 54.0]
c_strassen = [61.0, 432.0, 2708.0]

# ================================
# PLOT CONFIG
# ================================
fig, axs = plt.subplots(1, 3, figsize=(18, 5))
titles = ["Basic Multiplication", "Block Multiplication", "Strassen Algorithm"]

# --- SUBPLOT 1: BASIC ---
axs[0].plot(sizes, py_basic, marker='o', label='Python')
axs[0].plot(sizes, java_basic, marker='o', label='Java')
axs[0].plot(sizes, c_basic, marker='o', label='C')
axs[0].set_title(titles[0])
axs[0].set_xlabel("Matrix size (N×N)")
axs[0].set_ylabel("Time (ms)")
axs[0].grid(True)

# --- SUBPLOT 2: BLOCK ---
axs[1].plot(sizes, py_block, marker='o', label='Python')
axs[1].plot(sizes, java_block, marker='o', label='Java')
axs[1].plot(sizes, c_block, marker='o', label='C')
axs[1].set_title(titles[1])
axs[1].set_xlabel("Matrix size (N×N)")
axs[1].grid(True)

# --- SUBPLOT 3: STRASSEN ---
axs[2].plot(sizes, py_strassen, marker='o', label='Python')
axs[2].plot(sizes, java_strassen, marker='o', label='Java')
axs[2].plot(sizes, c_strassen, marker='o', label='C')
axs[2].set_title(titles[2])
axs[2].set_xlabel("Matrix size (N×N)")
axs[2].grid(True)

# --- COMMON LEGEND ---
plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1))

plt.tight_layout()
plt.show()

# Save figure
plt.savefig("multilanguage_comparison.png", dpi=300)
