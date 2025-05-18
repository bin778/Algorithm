const [A, B] = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(BigInt);
console.log([A + B, A - B, A * B].join("\n"));