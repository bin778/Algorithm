function solution(brown, yellow) {
    const area = brown + yellow;
    const measure = [];
    
    // 약수 구하기
    for (let i = 1; i <= area; i++) {
        if (area % i === 0) measure.push(i);
    }
    
    // 노란색 개수 구하기: (가로 - 2) * (세로 - 2) = 노란색 개수
    if (measure.length % 2 === 0) {
        for (let i = 0; i < measure.length / 2; i++) {
            if ((measure[i] - 2) * (measure[measure.length - (i + 1)] - 2) === yellow)
                return [measure[measure.length - (i + 1)], measure[i]];
        }
    }
    else return [measure[Math.floor(measure.length / 2)], measure[Math.floor(measure.length / 2)]];
}