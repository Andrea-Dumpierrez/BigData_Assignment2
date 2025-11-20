# Task 2 – Optimized Matrix Multiplication Approaches and Sparse Matrices
Course: Big Data  
Degree in Data Science and Engineering  
University of Las Palmas de Gran Canaria  

Author: Andrea Dumpiérrez Medina  
Date: November 2025

---

##  Project Description

This project investigates several approaches for matrix multiplication, including:
- The basic O(n³) algorithm  
- Optimized methods (Blocking/Tiling and Strassen)
- Sparse matrix multiplication using SciPy
- Performance comparison across Python, Java, and C
- Performance evaluation of a real large sparse matrix (mc2depi)

The project includes:
- Execution time measurements  
- Memory usage evaluation (Python)
- Comparison between dense and sparse matrices  
- Analysis of bottlenecks and limitations  

The complete written report can be found in:  
**`Task2_Memory_Andrea.pdf`**

---

##  Repository Structure

BigData_Assignment2/
│
├── c_code/ # C implementations and benchmark
│ ├── matrix_basic.c
│ ├── matrix_block.c
│ ├── matrix_strassen.c
│ └── benchmark_c.c
│
├── java_code/ # Java implementations and benchmark
│ ├── MatrixBasic.java
│ ├── MatrixBlock.java
│ ├── MatrixStrassen.java
│ └── Benchmark.java
│
├── py_code/ # Python implementations, plots and sparse tests
│ ├── matrix_basic.py
│ ├── matrix_block.py
│ ├── matrix_strassen.py
│ ├── matrix_sparse.py
│ ├── real_sparse_test.py
│ └── plots/ # Generated plots (.png)
│
├── mc2depi.mtx # Real-world sparse matrix (Matrix Market format)
│
├── Task2_Memory_Andrea.pdf # Final written report
│
└── README # This file



---

##  How to Run the Code

### **Python**
Requirements:
- Python 3.x  
- NumPy  
- SciPy  
- Matplotlib  

Install dependencies:
pip install numpy scipy matplotlib


Run the dense multiplication benchmarks:
python py_code/matrix_basic.py
python py_code/matrix_block.py
python py_code/matrix_strassen.py



Run sparse multiplication benchmark:
python py_code/matrix_sparse.py



Run real sparse matrix test:
python py_code/real_sparse_test.py



---

### **C Code**
Compile everything using GCC:

cd c_code
gcc benchmark_c.c matrix_basic.c matrix_block.c matrix_strassen.c -o benchmark_c
./benchmark_c



---

### **Java Code**
Compile:

cd java_code
javac *.java

makefile
Copiar código

Run:

java Benchmark



---

##  Generated Plots

All plots (.png) are located in:

py_code/plots/



These include:
- Comparison between Python, Java, C  
- Optimized methods in each language  
- Memory usage for Python  
- Dense vs sparse performance  
- SpMV on real matrix mc2depi  

---

##  Notes

- Sparse multiplication was only implemented in Python (SciPy), as explained in the report.
- Memory measurements were only performed in Python due to tool availability.
- Strassen becomes inefficient for small matrices (as expected).
- The real sparse matrix experiment validates the usefulness of CSR format.

---

##  Final Status

The project is fully completed and ready for evaluation.
For details, refer to the full PDF report.
