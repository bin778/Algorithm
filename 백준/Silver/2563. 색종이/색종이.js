const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);

const paper = Array.from(new Array(100), () => new Array(100).fill(0));
let result = 0;
const confetti = [];

const array = [];
for (let i = 0; i < N; i++) {
    array.push([]);
}

for (let i = 0; i < N; i++) {
    confetti.push(input[i+1].split(" ").map(Number));
}

for (let i = 0; i < N; i++) {
    const weight = confetti[i][0];
    const height = confetti[i][1];
    for (let j = weight; j < weight + 10; j++) {
        for (let k = height; k < height + 10; k++) {
            if (paper[j][k] === 0) {
                paper[j][k] = 1;
                result++;
            }
        }
    }
}

console.log(result);