function solution(n, s) {
    const result = [];
    if (n > s) return [-1];
    
    for (let i = n; i > 0; i--) {
        const num = Math.floor(s / i);
        result.push(num);
        s -= num;
    }
    return result;
}