// n 진법, t 숫자의 개수, m 인원, p 순서
function solution(n, t, m, p) {
    let result = '';
    let cnt = 0, turn = 0;
    p = p - 1;
    
    while (result.length !== t) {
        const notation = cnt.toString(n).toUpperCase();
        for (let i = 0; i < notation.length; i++) {
            if (turn % m === p) {
                result += notation[i];
            }
            if (result.length === t) break;
            turn++;
        }
        cnt++;
    }
    return result;
}