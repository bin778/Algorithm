import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> result = new ArrayList<>();
        
        for (int i = 0; i < commands.length; i++) {
            int lRange = commands[i][0], rRange = commands[i][1];
            int idx = commands[i][2];
            
            int[] sliceArr = Arrays.copyOfRange(array, lRange - 1, rRange);
            Arrays.sort(sliceArr);
            result.add(sliceArr[idx - 1]);
        }
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}