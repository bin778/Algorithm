let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(row => row.split(' ').map(i => Number(i)));

let result = "";
const zero = getZero();
dfs(0);

function check(x, y, n) {
	for (let i = 0; i < input.length; i++) {
    if (input[x][i] === n || input[i][y] === n) return false;
  }

	const X = Math.floor(x / 3) * 3;
	const Y = Math.floor(y / 3) * 3;

	for (let i = X; i < X + 3; i++) {
		for (let j = Y; j < Y + 3; j++) {
			if (input[i][j] == n) return false;
		}
	}
	return true;
}

function dfs(num) {
	if (num === zero.length) {
		for (let x of input) {
    		result += `${x.join(" ")}\n`;
    	}
    	console.log(result);
    	process.exit(0);
	}
	
	const [x, y] = zero[num];
	for (let i = 1; i < 10; i++) {
		if (check(x, y, i)) {
			input[x][y] = i;
			dfs(num + 1);
			input[x][y] = 0;
		}
	}
}

function getZero() {
  const arr = [];
  for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < input.length; j++) {
      if (input[i][j] === 0) arr.push([i, j]);
    }
  }
  return arr;
}