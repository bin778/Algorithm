import java.io.*;
import java.util.*;

public class Main {
    public static void generatePermutations(int[] arr, int size, int[] branch, int level, int num) {
        if (level == branch.length) {
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
        StringTokenizer nt = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(nt.nextToken());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = i + 1;
        }
        int M = Integer.parseInt(nt.nextToken());

        int[] branch = new int[M];
        generatePermutations(arr, N, branch, 0, 0);
    }
}