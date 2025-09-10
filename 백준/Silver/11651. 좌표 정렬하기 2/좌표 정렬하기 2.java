import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer numTokenizer = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(numTokenizer.nextToken());
        int[][] numArr =  new int[N][2];

        for (int i = 0; i < N; i++) {
            StringTokenizer arrTokenizer = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(arrTokenizer.nextToken());
            int y = Integer.parseInt(arrTokenizer.nextToken());
            numArr[i][0] = x;
            numArr[i][1] = y;
        }

        Arrays.sort(numArr, (x, y) -> {
            if (x[1] == y[1]) return x[0] - y[0];
            else return x[1] - y[1];
        });

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(numArr[i][0]).append(" ").append(numArr[i][1]).append("\n");
        }
        System.out.println(sb);
    }
}