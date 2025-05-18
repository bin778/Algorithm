function solution(k, m, score) {
    let result = 0;
    let box = [];
    score.sort((a, b) => b - a);

    for (let i of score) {
        box.push(i);
        if (box.length === m) {
            result += (Math.min(...box) * m);
            box = [];
        }
    }

    return result;
}