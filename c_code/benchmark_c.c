#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "matrix_basic.h"
#include "matrix_block.h"
#include "matrix_strassen.h"


// Measure execution time of functions with signature:
// double** f(double**, double**, int)
double measure_time(double** (*func)(double**, double**, int), double** A, double** B, int n) {
    clock_t start = clock();
    double** C = func(A, B, n);
    clock_t end = clock();

    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;

    // free result to prevent memory leaks
    free_matrix(C, n);

    return elapsed;
}

int main() {
    int sizes[] = {64, 128, 256};
    int num_sizes = 3;

    for (int s = 0; s < num_sizes; s++) {
        int n = sizes[s];
        printf("\n=== Matrix size: %dx%d ===\n", n, n);

        double** A = random_matrix(n);
        double** B = random_matrix(n);

        // BASIC
        double time_basic = measure_time(multiply_basic, A, B, n);
        printf("C Basic: %.4f s\n", time_basic);

        // BLOCK (using wrapper!)
        double time_block = measure_time(multiply_block_wrapper, A, B, n);
        printf("C Block: %.4f s\n", time_block);

        // STRASSEN
        double time_strassen = measure_time(strassen, A, B, n);
        printf("C Strassen: %.4f s\n", time_strassen);

        free_matrix(A, n);
        free_matrix(B, n);
    }

    return 0;
}
