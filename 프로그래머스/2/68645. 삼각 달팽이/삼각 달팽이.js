function solution(n) {
    const result = Array(n).fill().map((_, i) => Array(i + 1).fill(0));
    const size = n * (n + 1) / 2;
    let [i, j, cnt] = [0, 0, 1];
    
    while (cnt <= size) {
        // 세로 채우기
        while (i < n && !result[i][j])
            result[i++][j] = cnt++;
        i--; j++;
        // 가로 채우기
        while (j < n && !result[i][j])
            result[i][j++] = cnt++;
        i--; j -= 2;
        // 대각선 채우기
        while (i > 0 && j > 0 && !result[i][j])
            result[i--][j--] = cnt++;
        i += 2; j++;
    }
    
    return result.flat();
}