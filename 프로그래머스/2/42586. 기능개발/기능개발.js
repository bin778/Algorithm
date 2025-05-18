function solution(progresses, speeds) {
    const result = [];
    let i = 0, length = progresses.length;
    
    while (length) {
        let count = 0;
        progresses[i % length] += speeds[i % length];
        
        if (i++ % length === length - 1) {
            while (progresses[0] >= 100) {
                progresses.shift();
                speeds.shift();
                count++;
                length--;
                i = 0;
            }
        }
        if (count > 0) result.push(count);
    }
    return result;
}