function solution(n) {
    let result = 0;
    const board = new Array(n).fill(0);
    
    function nqueen(col, row, board) {
        for (let i = 0; i < col; i++) {
            if (board[i] === row) return false;
            if (Math.abs(col - i) === Math.abs(row - board[i])) return false;
        }
        return true;
    }
 
    function dfs(col, board) {
        const tmp = [...board];
        if (col === n) result++;

        for (let row = 0; row < n; row++) {
            if(nqueen(col, row, tmp)) {
                tmp[col] = row;
                dfs(col + 1, [...tmp]);
            }
        }
    }
    
    dfs(0, board);
    return result;
}