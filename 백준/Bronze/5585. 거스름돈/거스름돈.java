import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0, cnt = 0;
        int change = 1000 - N;
        int[] coin = {500, 100, 50, 10, 5, 1};

        while (change > 0) {
            if (change / coin[cnt] > 0) {
                change -= coin[cnt];
                result += 1;
            } else {
                cnt += 1;
            }
        }

        System.out.println(result);
    }
}