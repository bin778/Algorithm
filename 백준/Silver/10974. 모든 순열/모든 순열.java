import java.io.*;
import java.util.*;

public class Main {
    public static void generatePermutations(int[] arr, int size, int[] branch, int level, boolean[] visited) {
        if (level >= size - 1) {
            for (int i : branch) {
                System.out.print(i + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < size; i++) {
            if (!visited[i]) {
                branch[level += 1] = arr[i];
                visited[i] = true;
                generatePermutations(arr, size, branch, level, visited);
                visited[i] = false;
                level -= 1;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }
        boolean[] visited = new boolean[n];
        int[] branch = new int[n];
        generatePermutations(arr, n, branch, -1, visited);
    }
}