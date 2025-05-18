const input = require("fs").readFileSync("/dev/stdin").toString().split("-");

let result = input.reduce((total, item, idx) => {
    let sum = item
        .split("+")
        .map(Number)
        .reduce((total, cur) => total + cur);
    return idx === 0 ? total + sum : total - sum;
}, 0);
console.log(result);