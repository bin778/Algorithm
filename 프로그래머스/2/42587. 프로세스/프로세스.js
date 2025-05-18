function solution(priorities, location) {
    let max = Math.max(...priorities);
    const queue = [];
    const print = [];
    
    for (let i = 0; i < priorities.length; i++) {
        queue.push(String.fromCharCode(65 + i));
    }
    
    while (max !== 0) {
        // 최댓값이 없을 경우
        if (priorities.includes(max) === false) {
            max--;
            continue;
        }
        
        // 최댓값이 첫 번째에 들어 올때
        if (max === priorities[0]) {
            const char = queue.shift();
            const num = priorities.shift();
            print.push(char);
            if (priorities.includes(max) === false) max--;
            continue;
        }
        
        // queue 및 priorities 배열 이동하기
        const IndexChar = queue.shift();
        queue.push(IndexChar);
        const IndexNum = priorities.shift();
        priorities.push(IndexNum);
    }
    
    return print.indexOf(String.fromCharCode(65 + location)) + 1;
}