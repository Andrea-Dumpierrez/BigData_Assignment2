public class MatrixBasic {

    // Basic O(n^3) matrix multiplication
    public static double[][] multiplyBasic(double[][] A, double[][] B) {
        int n = A.length;
        double[][] C = new double[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                double sum = 0.0;
                for (int k = 0; k < n; k++) {
                    sum += A[i][k] * B[k][j];
                }
                C[i][j] = sum;
            }
        }
        return C;
    }

    // Utility: generate a random NxN matrix
    public static double[][] randomMatrix(int n) {
        double[][] M = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                M[i][j] = Math.random();
            }
        }
        return M;
    }

    // Small test
    public static void main(String[] args) {
        double[][] A = randomMatrix(3);
        double[][] B = randomMatrix(3);

        double[][] C = multiplyBasic(A, B);

        System.out.println("Basic multiplication completed.");
    }
}
