#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "matrix_basic.h"
#include "matrix_block.h"



// Blocked Matrix Multiplication
double** multiply_block(double** A, double** B, int n, int blockSize) {
    double** C = allocate_matrix(n);

    // Initialize matrix C to zero (IMPORTANT!)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = 0;
        }
    }

    // Block multiplication
    for (int ii = 0; ii < n; ii += blockSize) {
        for (int jj = 0; jj < n; jj += blockSize) {
            for (int kk = 0; kk < n; kk += blockSize) {

                int iMax = (ii + blockSize > n) ? n : ii + blockSize;
                int jMax = (jj + blockSize > n) ? n : jj + blockSize;
                int kMax = (kk + blockSize > n) ? n : kk + blockSize;

                for (int i = ii; i < iMax; i++) {
                    for (int j = jj; j < jMax; j++) {
                        double sum = 0;
                        for (int k = kk; k < kMax; k++) {
                            sum += A[i][k] * B[k][j];
                        }
                        C[i][j] += sum;
                    }
                }

            }
        }
    }

    return C;
}

// Wrapper so that multiply_block can be used in benchmark
double** multiply_block_wrapper(double** A, double** B, int n) {
    int blockSize = 16;  // You can use 8, 16, 32…
    return multiply_block(A, B, n, blockSize);
}


