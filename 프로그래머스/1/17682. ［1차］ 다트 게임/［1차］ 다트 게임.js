function solution(dartResult) {
    const dartResult2 = [...dartResult];
    const dartArr = [];
    
    // 점수, 보너스, 옵션을 분리하기
    for (let i = 1; i < dartResult2.length; i++) {
        if (isNaN(dartResult2[i - 1]) === false && isNaN(dartResult2[i]) === false) {
            dartArr.push(dartResult2[i - 1] + dartResult2[i]);
            i++;
        } else {
            dartArr.push(dartResult2[i - 1]);
        }
        if (i === dartResult2.length - 1) dartArr.push(dartResult2[i]);
    }

    const score = [];
    // 다트 점수 계산하기
    for (let i = 0; i < dartArr.length; i++) {
        // 숫자 더하기
        if (isNaN(dartArr[i]) === false) {
            i++;
            if (dartArr[i] === "S") score.push(Number(dartArr[i - 1]));
            else if (dartArr[i] === "D") score.push(Math.pow(Number(dartArr[i - 1]), 2));
            else if (dartArr[i] === "T") score.push(Math.pow(Number(dartArr[i - 1]), 3));
        }
        
        // 옵션 더하기
        if (dartArr[i] === "*") {
            for (let j = score.length - 2; j < score.length; j++) score[j] *= 2;
        } else if (dartArr[i] === "#") score[score.length - 1] *= -1;
    }
    
    let result = 0;
    // 다트 점수 합치기
    for (let i = 0; i < score.length; i++)
        result += score[i];
        
    return result;
}