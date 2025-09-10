class Solution {
    public boolean solution(int x) {
        int y = 0;
        String str = String.valueOf(x);
        for (int i = 0; i < str.length(); i++) 
            y += Character.getNumericValue(str.charAt(i));
        return x % y == 0 ? true : false;
    }
}