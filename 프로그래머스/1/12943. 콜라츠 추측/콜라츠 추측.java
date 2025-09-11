class Solution {
    public int solution(int num) {
        int result = 0;
        while (num != 1) {
            if (num % 2 == 0) num /= 2;
            else if (num % 2 == 1) num = num * 3 + 1;
            result++;
            
            if (result > 500 || num < 0) {
                result = -1;
                break;
            }
        }
        return result;
    }
}