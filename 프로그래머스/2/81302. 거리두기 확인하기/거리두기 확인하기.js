function getCombination(arr, select) {
    const result = [];
    if (select === 1) return arr.map((value) => [value]);
    
    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombination(rest, select - 1);
        const attached = combinations.map((combo) => [fixed, ...combo]);
        result.push(...attached);
    });
    
    return result;
}

function solution(places) {
    const result = new Array(places.length).fill(1);
    
    for (let room = 0; room < places.length; room++) {
        const P_arr = [];
        
        // 응시자(P)의 위치 확인하기
        for (let i = 0; i < places[room].length; i++) {
            for (let j = 0; j < places[room][i].length; j++) {
                if (places[room][i][j] === "P") P_arr.push([i, j]);
            }
        }
        
        // 응시자들의 조합을 구하기
        const P_combination = getCombination(P_arr, 2);
        
        for (let i = 0; i < P_combination.length; i++) {
            const [p1, p2] = P_combination[i];
            const [x1, y1] = p1;
            const [x2, y2] = p2;
            
            // 두 응시자끼리 거리 계산
            const distance = Math.abs(x1 - x2) + Math.abs(y1 - y2);
            
            // 거리가 1일 때
            if (distance === 1) {
                result[room] = 0;
                break;
            // 거리가 2일 때
            } else if (distance === 2) {
                if (x1 === x2) { // 행 사이에 파티션(X)이 있는 지 확인
                    if (places[room][x1][(y1 + y2) / 2] !== 'X') {
                        result[room] = 0;
                        break;
                    }
                } else if (y1 === y2) { // 열 사이에 파티션(X)이 있는 지 확인
                    if (places[room][(x1 + x2) / 2][y1] !== 'X') {
                        result[room] = 0;
                        break;
                    }
                } else { // 대각선에 파티션(X)이 있는 지 확인
                        if (places[room][x1][y2] !== 'X' || places[room][x2][y1] !== 'X') {
                        result[room] = 0;
                        break;
                    }
                }
            }
        }
    }
    return result;
}