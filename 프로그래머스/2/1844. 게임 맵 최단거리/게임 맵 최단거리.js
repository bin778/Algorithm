// BFS 사용 예시
const dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]; // 상하좌우 좌표

function bfs(maps) {
    const rowLen = maps.length; // 행 길이
    const colLen = maps[0].length; // 열 길이
    
    let queue = [[0, 0, 1]]; // 행 위치, 열 위치, 이동 거리
    let front = 0; // 큐의 시작 인덱스

    while (front < queue.length) {
        const [curRow, curCol, dist] = queue[front++];
        maps[curRow][curCol] = 0; // 플레이어가 이동한 구간은 0으로 초기화
        
        // 적 팀 진영으로 이동하면 dist 리턴
        if (curRow === rowLen - 1 && curCol === colLen - 1) return dist;
        
        // 상하좌우 이동 여부 확인
        for (let [r, c] of dir) {
            // 현재 위치에서 상하좌우로 이동한 새로운 위치
            let newRow = curRow + r;
            let newCol = curCol + c;
            
            // 새로운 위치이면서 벽이 아닐 시 이동 가능
            if (newRow >= 0 && newRow < rowLen && newCol >= 0 && newCol < colLen && maps[newRow][newCol] === 1) {
                queue.push([newRow, newCol, dist + 1]);
                maps[newRow][newCol] = 0; // 새로운 위치는 0으로 표시
            }
        }
    }
    return -1;
}

function solution(maps) {
    return bfs(maps);
}