const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);
let result = 0;
const board = new Array(N).fill(0);
 
function nqueen(col, row, board) {
	for (let i = 0; i < col; i++) {
		if (board[i] === row) return false;
		if (Math.abs(col - i) === Math.abs(row - board[i])) return false;
	}
	return true;
}
 
function dfs(col, board) {
	const tmp = [...board];
	if (col === N) result++;
 
	for (let row = 0; row < N; row++) {
		if(nqueen(col, row, tmp)) {
			tmp[col] = row;
			dfs(col + 1, [...tmp]);
		}
	}
}
 
dfs(0, board);
console.log(result);