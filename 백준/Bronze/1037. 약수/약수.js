const input = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");

const N = parseInt(input[0]);
const arr = input[1].split(' ').sort((a, b) => a - b);
const max = Math.max(...arr);
const min = Math.min(...arr);
let result = 0;

(arr.length >= 2) ? (result = max * min) : (result = min *min);
console.log(result);