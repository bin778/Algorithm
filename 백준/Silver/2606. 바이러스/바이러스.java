import java.io.*;
import java.util.*;

public class Main {
    private static int result = 0;
    private static ArrayList<ArrayList<Integer>> graph;
    private static boolean[] visited;

    public static void DFS(int nodeNum) {
        visited[nodeNum] = true;
        result += 1;

        for (int child : graph.get(nodeNum)) {
            if (!visited[child]) {
                DFS(child);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int com = Integer.parseInt(br.readLine());
        int edge = Integer.parseInt(br.readLine());

        graph = new ArrayList<>();
        for (int i = 0; i < com; i++) {
            graph.add(new ArrayList<>());
        }

        visited = new boolean[com];

        for (int i = 0; i < edge; i++) {
            String[] size = br.readLine().split(" ");
            int u = Integer.parseInt(size[0]) - 1;
            int v = Integer.parseInt(size[1]) - 1;

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        DFS(0);
        System.out.println(result - 1);
    }
}