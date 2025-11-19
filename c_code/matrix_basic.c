#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "matrix_basic.h"



// Allocate an NxN matrix
double** allocate_matrix(int n) {
    double** M = malloc(n * sizeof(double*));
    for (int i = 0; i < n; i++) {
        M[i] = malloc(n * sizeof(double));
    }
    return M;
}

// Free NxN matrix
void free_matrix(double** M, int n) {
    for (int i = 0; i < n; i++) {
        free(M[i]);
    }
    free(M);
}


// Generate random NxN matrix
double** random_matrix(int n) {
    double** M = allocate_matrix(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            M[i][j] = rand() % 10;
        }
    }
    return M;
}

// Basic Matrix Multiplication
double** multiply_basic(double** A, double** B, int n) {
    double** C = allocate_matrix(n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            double sum = 0;
            for (int k = 0; k < n; k++) {
                sum += A[i][k] * B[k][j];
            }
            C[i][j] = sum;
        }
    }
    return C;
}

