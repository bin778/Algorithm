import java.io.*;
import java.util.*;

public class Main {
    public static int lotto_num = 6;
    public static void generatePermutations(int[] arr, int size, int[] branch, int level, int num) {
        if (level == lotto_num) {
            for (int i : branch) {
                System.out.print(i + " ");
            }
            System.out.println();
            return;
        }

        for (int i = num; i < size; i++) {
            branch[level] = arr[i];
            generatePermutations(arr, size, branch, level + 1, i + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = br.readLine()) != null) {
            StringTokenizer nt = new StringTokenizer(line, " ");

            if (!nt.hasMoreTokens()) {
                continue;
            }

            int n = Integer.parseInt(nt.nextToken());
            if (n == 0) break;
            
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(nt.nextToken());
            }

            int[] branch = new int[lotto_num];
            generatePermutations(arr, n, branch, 0, 0);
            System.out.println();
        }
    }
}