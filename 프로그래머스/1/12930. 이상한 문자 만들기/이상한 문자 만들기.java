import java.util.*;

class Solution {
    public String solution(String s) {
        s += " ";
        int idx = 0;
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == ' ') idx = 0;
            else idx += 1;
            
            if (idx > 0 && idx % 2 == 0) result.append(Character.toLowerCase(s.charAt(i)));
            else if (idx > 0 && idx % 2 == 1) result.append(Character.toUpperCase(s.charAt(i)));
            else result.append(" ");
        }
        return result.toString();
    }
}