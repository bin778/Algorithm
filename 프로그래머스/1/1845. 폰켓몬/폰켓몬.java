import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int maxCnt = nums.length / 2;
        
        Set<Integer> uniquePokemon = new HashSet<>();
        for (int num : nums) {
            uniquePokemon.add(num);
        }
        
        System.out.println(uniquePokemon);
        
        int pokemonVC = uniquePokemon.size();
        
        return Math.min(pokemonVC, maxCnt);
    }
}