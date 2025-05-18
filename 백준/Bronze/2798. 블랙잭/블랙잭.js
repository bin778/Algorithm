const input = require("fs").readFileSync("dev/stdin").toString().trim().split("\n");
input[0] = input[0].trim().split(" ");
const N = Number(input[0][0]);
const M = Number(input[0][1]);
const cards = input[1].trim().split(" ").map(Number);

let result = 0;

for (let i = 0; i < N - 2; i++) {
    for (let j = i + 1; j < N - 1; j++) {
        for (let k = j + 1; k < N; k++) {
            let tmp = cards[i] + cards[j] + cards[k];
            if (M >= tmp && tmp-result > 0) result = tmp;
        }
    }
}
console.log(result);