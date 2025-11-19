#include <stdio.h>
#include <stdlib.h>
#include "matrix_basic.c"
#include "matrix_strassen.c"

// Compare two matrices
int compare(double** A, double** B, int n) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (abs(A[i][j] - B[i][j]) > 1e-6)
                return 0;
    return 1;
}

int main() {
    int n = 4;   // small test

    double** A = random_matrix(n);
    double** B = random_matrix(n);

    double** C_basic = multiply_basic(A, B, n);
    double** C_strassen = strassen(A, B, n);

    printf("Strassen correct: %s\n", compare(C_basic, C_strassen, n) ? "true" : "false");

    return 0;
}
