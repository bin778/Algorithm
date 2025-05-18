function solution(operations) {
    let arr = [];
    for (let op of operations) {
        const [com, numStr] = op.split(" ");
        const num = parseInt(numStr);
        
        if (com === "I") {
            arr.push(num);
        } else if (com === "D") {
            if (num === 1)
                arr.pop();
            else if (num === -1)
                arr.shift();
        }
        arr.sort((a, b) => (a - b));
    }
    return arr.length ? [Math.max(...arr), Math.min(...arr)] : [0, 0];
}