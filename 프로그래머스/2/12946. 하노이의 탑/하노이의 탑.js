let result = [];
function hanoi(num, from, other, to) {
    if (num === 0) return;
    else {
        hanoi(num - 1, from, to, other);
        result.push([from, to]);
        hanoi(num - 1, other, from, to);
    }
}

function solution(n) {
    hanoi(n, 1, 2, 3);
    return result;
}