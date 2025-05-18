function solution(survey, choices) {
    // 1번: 라이언형(R) 튜브형(T)
    const personality1 = [0, 0];
    // 2번: 콘형(C) 프로도형(F)
    const personality2 = [0, 0];
    // 3번: 제이지형(J) 무지형(M)
    const personality3 = [0, 0];
    // 4번: 어피치형(A) 네오형(N)
    const personality4 = [0, 0];
    let result = '';
    
    // 성격 유형 점수 추가
    for (let i = 0; i < survey.length; i++) {
        switch (survey[i]) {
            case "RT":
                if (choices[i] <= 3) personality1[0] += (4 - choices[i]);
                else if (choices[i] >= 5) personality1[1] += (choices[i] - 4);
                break;
            case "TR":
                if (choices[i] <= 3) personality1[1] += (4 - choices[i]);
                else if (choices[i] >= 5) personality1[0] += (choices[i] - 4);
                break;
            case "CF":
                if (choices[i] <= 3) personality2[0] += (4 - choices[i]);
                else if (choices[i] >= 5) personality2[1] += (choices[i] - 4);
                break;
            case "FC":
                if (choices[i] <= 3) personality2[1] += (4 - choices[i]);
                else if (choices[i] >= 5) personality2[0] += (choices[i] - 4);
                break;
            case "JM":
                if (choices[i] <= 3) personality3[0] += (4 - choices[i]);
                else if (choices[i] >= 5) personality3[1] += (choices[i] - 4);
                break;
            case "MJ":
                if (choices[i] <= 3) personality3[1] += (4 - choices[i]);
                else if (choices[i] >= 5) personality3[0] += (choices[i] - 4);
                break;
            case "AN":
                if (choices[i] <= 3) personality4[0] += (4 - choices[i]);
                else if (choices[i] >= 5) personality4[1] += (choices[i] - 4);
                break;
            case "NA":
                if (choices[i] <= 3) personality4[1] += (4 - choices[i]);
                else if (choices[i] >= 5) personality4[0] += (choices[i] - 4);
                break;
        }
    }
    
    // 결과 값 반환하기
    if (personality1[0] >= personality1[1]) result += 'R';
    else result += 'T';
    if (personality2[0] >= personality2[1]) result += 'C';
    else result += 'F';
    if (personality3[0] >= personality3[1]) result += 'J';
    else result += 'M';
    if (personality4[0] >= personality4[1]) result += 'A';
    else result += 'N';
    
    return result;
}