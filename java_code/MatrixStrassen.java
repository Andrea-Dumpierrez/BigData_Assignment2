public class MatrixStrassen {

    // Add two matrices
    public static double[][] add(double[][] A, double[][] B) {
        int n = A.length;
        double[][] C = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = A[i][j] + B[i][j];
            }
        }
        return C;
    }

    // Subtract two matrices
    public static double[][] subtract(double[][] A, double[][] B) {
        int n = A.length;
        double[][] C = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = A[i][j] - B[i][j];
            }
        }
        return C;
    }

    // Copy submatrix (from [row:row+k], [col:col+k])
    public static double[][] copyBlock(double[][] M, int row, int col, int size) {
        double[][] block = new double[size][size];
        for (int i = 0; i < size; i++) {
            System.arraycopy(M[row + i], col, block[i], 0, size);
        }
        return block;
    }

    // Insert block into matrix
    public static void insertBlock(double[][] M, double[][] block, int row, int col) {
        int size = block.length;
        for (int i = 0; i < size; i++) {
            System.arraycopy(block[i], 0, M[row + i], col, size);
        }
    }

    // Base multiplication
    public static double[][] basicMultiply(double[][] A, double[][] B) {
        int n = A.length;
        double[][] C = new double[n][n];
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

    // Strassen algorithm
    public static double[][] strassen(double[][] A, double[][] B) {
        int n = A.length;

        // Base case
        if (n <= 64)
            return basicMultiply(A, B);

        int k = n / 2;

        // Split into blocks
        double[][] A11 = copyBlock(A, 0, 0, k);
        double[][] A12 = copyBlock(A, 0, k, k);
        double[][] A21 = copyBlock(A, k, 0, k);
        double[][] A22 = copyBlock(A, k, k, k);

        double[][] B11 = copyBlock(B, 0, 0, k);
        double[][] B12 = copyBlock(B, 0, k, k);
        double[][] B21 = copyBlock(B, k, 0, k);
        double[][] B22 = copyBlock(B, k, k, k);

        // Strassen operations
        double[][] M1 = strassen(add(A11, A22), add(B11, B22));
        double[][] M2 = strassen(add(A21, A22), B11);
        double[][] M3 = strassen(A11, subtract(B12, B22));
        double[][] M4 = strassen(A22, subtract(B21, B11));
        double[][] M5 = strassen(add(A11, A12), B22);
        double[][] M6 = strassen(subtract(A21, A11), add(B11, B12));
        double[][] M7 = strassen(subtract(A12, A22), add(B21, B22));

        // Combine blocks
        double[][] C11 = add(subtract(add(M1, M4), M5), M7);
        double[][] C12 = add(M3, M5);
        double[][] C21 = add(M2, M4);
        double[][] C22 = add(subtract(add(M1, M3), M2), M6);

        // Build result matrix
        double[][] C = new double[n][n];
        insertBlock(C, C11, 0, 0);
        insertBlock(C, C12, 0, k);
        insertBlock(C, C21, k, 0);
        insertBlock(C, C22, k, k);

        return C;
    }

    // Small test
    public static void main(String[] args) {

        double[][] A = MatrixBasic.randomMatrix(8);
        double[][] B = MatrixBasic.randomMatrix(8);

        double[][] C_strassen = strassen(A, B);
        double[][] C_basic = MatrixBasic.multiplyBasic(A, B);

        boolean ok = true;

        for (int i = 0; i < C_strassen.length; i++) {
            for (int j = 0; j < C_strassen.length; j++) {
                if (Math.abs(C_strassen[i][j] - C_basic[i][j]) > 1e-6) {
                    ok = false;
                    break;
                }
            }
        }

        System.out.println("Strassen correct: " + ok);
    }
}