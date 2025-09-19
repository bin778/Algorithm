import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int result = 0, cnt = 0;
        ArrayList<Integer> coin = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            coin.add(Integer.parseInt(br.readLine()));
        }

        Collections.reverse(coin);

        while (K > 0) {
            if (K / coin.get(cnt) > 0) {
                K -= coin.get(cnt);
                result += 1;
            } else {
                cnt += 1;
            }
        }
        System.out.println(result);
    }
}