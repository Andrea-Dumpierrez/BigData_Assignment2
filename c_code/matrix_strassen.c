#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "matrix_basic.h"
#include "matrix_strassen.h"


// Add two NxN matrices
double** add_matrix(double** A, double** B, int n) {
    double** C = allocate_matrix(n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
    return C;
}

// Subtract two NxN matrices
double** subtract_matrix(double** A, double** B, int n) {
    double** C = allocate_matrix(n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] - B[i][j];
    return C;
}

// Copy submatrix (block) from A into B
void copy_block(double** src, double** dst, int row, int col, int size) {
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            dst[i][j] = src[row + i][col + j];
}

// Write block into destination matrix at position (row, col)
void write_block(double** dst, double** block, int row, int col, int size) {
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            dst[row + i][col + j] = block[i][j];
}

// Strassen multiplication (recursive)
double** strassen(double** A, double** B, int n) {

    // BASE CASE (only multiply 1x1)
    if (n == 1) {
        double** C = allocate_matrix(1);
        C[0][0] = A[0][0] * B[0][0];
        return C;
    }

    int k = n / 2;

    // Allocate submatrices
    double** A11 = allocate_matrix(k);
    double** A12 = allocate_matrix(k);
    double** A21 = allocate_matrix(k);
    double** A22 = allocate_matrix(k);

    double** B11 = allocate_matrix(k);
    double** B12 = allocate_matrix(k);
    double** B21 = allocate_matrix(k);
    double** B22 = allocate_matrix(k);

    // Copy blocks correctly
    copy_block(A, A11, 0,   0,   k);
    copy_block(A, A12, 0,   k,   k);
    copy_block(A, A21, k,   0,   k);
    copy_block(A, A22, k,   k,   k);

    copy_block(B, B11, 0,   0,   k);
    copy_block(B, B12, 0,   k,   k);
    copy_block(B, B21, k,   0,   k);
    copy_block(B, B22, k,   k,   k);

    // Compute the 7 Strassen products
    double** M1 = strassen(add_matrix(A11, A22, k), add_matrix(B11, B22, k), k);
    double** M2 = strassen(add_matrix(A21, A22, k), B11, k);
    double** M3 = strassen(A11, subtract_matrix(B12, B22, k), k);
    double** M4 = strassen(A22, subtract_matrix(B21, B11, k), k);
    double** M5 = strassen(add_matrix(A11, A12, k), B22, k);
    double** M6 = strassen(subtract_matrix(A21, A11, k), add_matrix(B11, B12, k), k);
    double** M7 = strassen(subtract_matrix(A12, A22, k), add_matrix(B21, B22, k), k);

    // Compute C11, C12, C21, C22
    double** C11 = add_matrix(
                    subtract_matrix(add_matrix(M1, M4, k), M5, k),
                    M7,
                    k);

    double** C12 = add_matrix(M3, M5, k);
    double** C21 = add_matrix(M2, M4, k);
    double** C22 = add_matrix(subtract_matrix(add_matrix(M1, M3, k), M2, k), M6, k);

    // Allocate result matrix
    double** C = allocate_matrix(n);

    // Write blocks into C
    write_block(C, C11, 0, 0, k);
    write_block(C, C12, 0, k, k);
    write_block(C, C21, k, 0, k);
    write_block(C, C22, k, k, k);

        return C;

    
}
