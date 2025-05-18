function solution(m, n, puddles) {
    const DP = Array.from(Array(n + 1), () => Array(m + 1).fill(0));
    DP[1][1] = 1;
    
    for (let puddle of puddles)
        DP[puddle[1]][puddle[0]] = -1;
    
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            if (i === 1 && j === 1) continue;
            if (DP[i][j] === -1) DP[i][j] = 0;
            else DP[i][j] = (DP[i - 1][j] + DP[i][j - 1]) % 1000000007;
        }
    }
    return DP[n][m];
}