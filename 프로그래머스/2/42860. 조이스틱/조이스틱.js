// 최소 알파벳 변경 횟수 계산
function changeCount(char) {
    const up = char.charCodeAt() - "A".charCodeAt();
    const down = "Z".charCodeAt() - char.charCodeAt() + 1;
    return Math.min(up, down);
}

function solution(name) {
    let result = 0; // 최소 이동 거리
    let idx = 0; // 커서 위치
    
    // 각 문자를 변경하는 최소 횟수 계산
    for (let i = 0; i < name.length; i++) {
        result += changeCount(name[i]);
    }
    
    // 최소 커서 이동 거리 계산
    let move = name.length - 1;
    
    for (let i = 0; i < name.length; i++) {
        let next = i + 1;
        
        // A가 연속된 구간을 찾음
        while (next < name.length && name[next] === 'A') {
            next++;
        }
        
        // 현재 까지의 거리 + 연속된 A구간 이후의 최소 거리 계산
        move = Math.min(move, i + name.length - next + Math.min(i, name.length - next));
    }
    
    return result + move;
}