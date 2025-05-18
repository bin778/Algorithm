const [a, b] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(BigInt);

const result = (a, b) => {
    return a / b + '\n' + a % b
}

console.log(result(a, b));