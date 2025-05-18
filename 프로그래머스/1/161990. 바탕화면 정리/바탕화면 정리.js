function solution(wallpaper) {
    // 진짜 나 병X인가 그냥 좌표를 하나씩 하나씩 구해서
    // 가장 왼쪽, 오른쪽, 위쪽, 아래쪽에 있는 "#"을 구하면 될 것을 
    // 좌표를 한꺼번에 구할려 하네ㅋㅋㅋㅋ
    
    let S1 = wallpaper.length, S2 = wallpaper[0].length;
    let E1 = 0, E2 = 0;
    
    // 가로와 세로 길이
    const length = wallpaper.length;
    const width = wallpaper[0].length;
    
    // S1, E1 좌표 찍기
    for (let i = 0; i < wallpaper.length; i++) {
        if (wallpaper[i].includes("#") && (S1 > i)) S1 = i;
        if (wallpaper[i].includes("#") && (E1 < i)) E1 = i;
    }
    
    // S2, E2 좌표 찍기
    for (let i = 0; i < wallpaper[0].length; i++) {
        const temp = []
        for (let j = 0; j < wallpaper.length; j++) {
            temp.push(wallpaper[j][i]);
        }
        if (temp.includes("#") && (S2 > i)) S2 = i;
        if (temp.includes("#") && (E2 < i)) E2 = i;
    }
    
    return [S1, S2, E1 + 1, E2 + 1];
}