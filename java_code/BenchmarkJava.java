public class BenchmarkJava {

    // Measure execution time in milliseconds
    public static long measureTime(Runnable function) {
        long start = System.nanoTime();
        function.run();
        long end = System.nanoTime();
        return (end - start) / 1_000_000; // convert to ms
    }

    // Generate a random NxN matrix
    public static double[][] randomMatrix(int n) {
        double[][] M = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                M[i][j] = Math.random();
            }
        }
        return M;
    }

    public static void main(String[] args) {
        int[] sizes = {64, 128, 256};

        for (int n : sizes) {
            System.out.println("\n=== Matrix size: " + n + "x" + n + " ===");

            double[][] A = randomMatrix(n);
            double[][] B = randomMatrix(n);

            long timeBasic = measureTime(() -> {
                MatrixBasic.multiplyBasic(A, B);
            });

            System.out.println("Java Basic: " + timeBasic + " ms");
        }
    }
}
