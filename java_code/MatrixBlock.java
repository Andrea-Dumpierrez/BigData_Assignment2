public class MatrixBlock {

    // Blocked (cache-friendly) matrix multiplication
    public static double[][] multiplyBlock(double[][] A, double[][] B, int blockSize) {
        int n = A.length;
        double[][] C = new double[n][n];

        for (int i = 0; i < n; i += blockSize) {
            for (int j = 0; j < n; j += blockSize) {
                for (int k = 0; k < n; k += blockSize) {

                    int iEnd = Math.min(i + blockSize, n);
                    int jEnd = Math.min(j + blockSize, n);
                    int kEnd = Math.min(k + blockSize, n);

                    for (int ii = i; ii < iEnd; ii++) {
                        for (int jj = j; jj < jEnd; jj++) {
                            double sum = 0;
                            for (int kk = k; kk < kEnd; kk++) {
                                sum += A[ii][kk] * B[kk][jj];
                            }
                            C[ii][jj] += sum;
                        }
                    }

                }
            }
        }

        return C;
    }

    // Small test
    public static void main(String[] args) {

        double[][] A = MatrixBasic.randomMatrix(8);
        double[][] B = MatrixBasic.randomMatrix(8);

        double[][] C_block = multiplyBlock(A, B, 4);
        double[][] C_basic = MatrixBasic.multiplyBasic(A, B);

        boolean ok = true;

        for (int i = 0; i < C_block.length; i++) {
            for (int j = 0; j < C_block.length; j++) {
                if (Math.abs(C_block[i][j] - C_basic[i][j]) > 1e-6) {
                    ok = false;
                    break;
                }
            }
        }

        System.out.println("Block correct: " + ok);
    }
}
