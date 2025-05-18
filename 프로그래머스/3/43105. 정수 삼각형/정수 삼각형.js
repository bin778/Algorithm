function solution(triangle) {
    const dp = Array.from({ length: triangle.length }, (_, i) => Array(i + 1).fill(0));
    dp[0][0] = triangle[0][0];
    
    for (let i = 1; i < triangle.length; i++) {
        for (let j = 0; j < triangle[i].length; j++) {
            if (j - 1 >= 0)
                dp[i][j] = Math.max(dp[i][j], triangle[i][j] + dp[i - 1][j - 1]);
            if (j < i)
                dp[i][j] = Math.max(dp[i][j], triangle[i][j] + dp[i - 1][j]);
        }
    }
    return Math.max(...dp[dp.length - 1]);
}