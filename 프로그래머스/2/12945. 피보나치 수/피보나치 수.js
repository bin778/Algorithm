function solution(n) {
    let result = 0;
    
    // 피보나치 0, 1 설정
    let FN2 = 0;
    let FN1 = 1;
    
    // 피보나치 반복문 돌리기
    for (let i = 2; i <= n; i++) {
        result = FN2 % 1234567 + FN1 % 1234567;
        FN2 = FN1 % 1234567;
        FN1 = result % 1234567;
    }
    
    return result % 1234567;
}