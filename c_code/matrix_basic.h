#ifndef MATRIX_BASIC_H
#define MATRIX_BASIC_H

double** allocate_matrix(int n);
void free_matrix(double** M, int n);
double** random_matrix(int n);
double** multiply_basic(double** A, double** B, int n);

#endif
