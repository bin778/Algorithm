function solution(n, m, section) {
    let result = 0;
    let max = 0;
    
    for (let i of section) {
        if (i > max) {
            result++;
            max = i + m - 1;
        }
    }
    
    return result;
}