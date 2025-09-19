import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        int[] coin = {2, 5};

        while (N > 0) {
            if (N % coin[1] == 0) {
                N -= coin[1];
                result += 1;
                continue;
            }
            N -= coin[0];
            result += 1;
        }

        System.out.println(N == 0 ? result : -1);
    }
}