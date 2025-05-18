const input = require("fs").readFileSync("dev/stdin").toString().trim().split("\n");
let [N, M] = input[0].split(' ').map(Number);
let noListen = new Set(input.slice(1, N + 1));
let noSee = input.slice(N + 1);
const result = [];
for (let i = 0; i < M; i++) {
    if(noListen.has(noSee[i])){
    result.push(noSee[i]);
  }
}
result.sort();
console.log(result.length);
console.log(result.join("\n"));