function solution(N, stages) {
    const result = [], fail = [];
    let player = stages.length;
    
    // 실패율 구하기
    for (let i = 1; i <= N; i++) {
        let fail_player = 0;
        for (let j = 0; j < stages.length; j++) {
            if (i === stages[j]) fail_player++;
        }
        fail.push(fail_player / player);
        player -= fail_player;
    }
    
    // NaN 값 처리하기
    for (let i = 0; i < fail.length; i++) {
        if (isNaN(fail[i])) fail[i] = 0;
    }
    
    // 실패율 큰 순서대로 정렬하기
    for (let i = 0; i < fail.length; i++) {
        result.push(fail.indexOf(Math.max(...fail)) + 1);
        fail[fail.indexOf(Math.max(...fail))] = -1;
    }
    
    return result;
}