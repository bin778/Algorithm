function solution(sizes) {
    let max_w = 0;
    let max_h = 0;
    
    // 명함 뒤집기
    for (let i = 0; i < sizes.length; i++) {
        let temp = 0;
        if (sizes[i][0] < sizes[i][1]) {
            temp = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = temp;
        }
    }
    
    // 최댓값 구하기
    for (let i = 0; i < sizes.length; i++) {
        if (sizes[i][0] > max_w) max_w = sizes[i][0];
        if (sizes[i][1] > max_h) max_h = sizes[i][1];
    }
    
    return max_w * max_h;
}