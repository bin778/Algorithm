const input = require("fs").readFileSync("dev/stdin").toString().trim().split("\n");
const [row, col] = input[0].split(" ").map((v) => +v);
const maps = [];
for (let i = 1; i <= row; i++) maps.push(input[i].split("").map((v) => +v));
const checked = Array.from({ length: row }, () => Array(col).fill(0));

const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];
const queue = [[0, 0]];
    
checked[0][0] = 1;
while (queue.length) {
    const [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
        const nx = x + dx[i], ny = y + dy[i];
        if (nx < 0 || ny < 0 || nx >= row || ny >= col) continue;
        if (maps[nx][ny] && !checked[nx][ny]) {
            checked[nx][ny] = checked[x][y] + 1;
            queue.push([nx, ny]);
        }
    }
}
const result = checked[row - 1][col - 1] ? checked[row - 1][col - 1] : -1;
console.log(result);