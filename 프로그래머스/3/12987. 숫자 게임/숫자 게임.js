function solution(A, B) {
    let result = 0;
    A.sort((x, y) => (x - y));
    B.sort((x, y) => (x - y));
    let idxA = 0;
    let idxB = 0;
    
    while (idxA < A.length && idxB < B.length) {
        if (A[idxA] < B[idxB]) {
            result += 1;
            idxA += 1
            idxB += 1
        } else {
            idxB += 1
        }
    }
    
    return result;
}