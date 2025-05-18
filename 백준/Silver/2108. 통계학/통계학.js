const input = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n").map((num) => parseInt(num));
const N = input.shift();
const num = input.sort((a, b) => a - b);

// 산술평균 구하기
const avr = Math.round(input.reduce((acc, num) => (acc += num), 0) / N);
console.log(avr.toString());

// 중앙값 구하기
console.log(num[Math.floor(N / 2)]);

// 최빈값 구하기
let max = 0;

const map = new Map();

for (let i of num) {
	if (map.get(i)) {
		map.set(i, map.get(i) + 1);
	} else {
		map.set(i, 1);
	}
	if (map.get(i) > max) max = map.get(i);
}

let freq = [];
for (let i of new Set(num)) {
	if (map.get(i) === max) freq.push(i);
}

freq.length > 1 ? console.log(freq[1]) : console.log(freq[0]);

// 범위 구하기
console.log((num[N - 1] - num[0]));