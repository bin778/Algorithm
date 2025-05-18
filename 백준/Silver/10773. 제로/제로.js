const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const K = input[0];
let result = 0
const stack = []

for (let i = 1; i <= K; i++) {
	const num = Number(input[i]);
	
	if (num === 0) {
		const top = stack.pop();
		result -= top;
	} else {
		stack.push(num);
		result += num;
	}
}

console.log(result);