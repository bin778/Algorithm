function solution(X, Y) {
    const idxArr = new Array(10).fill(0);
    let result = [];
    
    // 숫자 짝꿍 찾기
    for (let i = 0; i < X.length; i++) {
        let idx = Y.indexOf(X[i], idxArr[X[i]]);
        if (idx === -1) continue;
        result.push(X[i]);
        idxArr[X[i]] = idx + 1;
    }
    
    if (result[0] === "0") return "0";
    else return !result.length ? "-1" : result.sort((a, b) => (b - a)).join("");
}