public class BenchmarkJavaFull {

    public static long measureTime(Runnable func) {
        long start = System.nanoTime();
        func.run();
        long end = System.nanoTime();
        return (end - start) / 1_000_000; // convert to ms
    }

    public static double[][] randomMatrix(int n) {
        return MatrixBasic.randomMatrix(n);
    }

    public static void main(String[] args) {

        int[] sizes = {64, 128, 256};

        for (int n : sizes) {
            System.out.println("\n=== Matrix size: " + n + "x" + n + " ===");

            double[][] A = randomMatrix(n);
            double[][] B = randomMatrix(n);

            // Basic
            long tBasic = measureTime(() -> {
                MatrixBasic.multiplyBasic(A, B);
            });
            System.out.println("Java Basic: " + tBasic + " ms");

            // Block
            long tBlock = measureTime(() -> {
                MatrixBlock.multiplyBlock(A, B, 32);
            });
            System.out.println("Java Block: " + tBlock + " ms");

            // Strassen (only works well for powers of 2)
            long tStrassen = measureTime(() -> {
                MatrixStrassen.strassen(A, B);
            });
            System.out.println("Java Strassen: " + tStrassen + " ms");
        }
    }
}
