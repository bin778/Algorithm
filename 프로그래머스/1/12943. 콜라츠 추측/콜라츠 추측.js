function solution(num) {
    let result = 0;
    while (num !== 1 && result !== 500) {
        num = num % 2 === 0 ? num / 2 : num * 3 + 1;
        result++;
    }
    return result >= 500 ? -1 : result;
}