class Solution {
    public int solution(int n) {
        int root = (int)Math.sqrt(n);
        int result = 0;
    
        for (int i = 1; i <= root; i++)
        if (n % i == 0) {
            result += i;
            if (n / i != i)
                result += (int)n / i;
            }
    
    return result;
    }
}