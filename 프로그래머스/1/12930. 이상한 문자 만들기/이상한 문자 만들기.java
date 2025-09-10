import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder result = new StringBuilder();
        String[] words = s.split(" ") + " ";
        System.out.println(words[2]);
        
        for (String word : words) {
            if (!word.equals(""))
                for (int idx = 0; idx < word.length(); idx++) {
                    if (word.charAt(idx) % 2 == 0) {
                        result.append(word.charAt(idx));
                    }
                    else result.append(word.charAt(idx));
                }
            else continue;
            
        }
        return result.toString();
    }
}