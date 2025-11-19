#ifndef MATRIX_BLOCK_H
#define MATRIX_BLOCK_H

double** multiply_block(double** A, double** B, int n, int blockSize);
double** multiply_block_wrapper(double** A, double** B, int n);

#endif
