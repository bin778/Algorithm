function solution(rows, columns, queries) {
    const result = [];
    const matrix = [];
    
    // row * columns 만큼의 가변 배열 만들기
    let cnt = 1;
    for (let i = 0; i < rows; i++) {
        let temp = [];
        for (let j = 0; j < columns; j++)
            temp.push(cnt++);
        matrix.push(temp);
    }
    
    for (let que of queries) {
        let x1 = que[0] - 1, y1 = que[1] - 1, x2 = que[2] - 1, y2 = que[3] - 1;
        const new_matrix = [];
        
        // 회전할 숫자를 배열에 따로 넣는다
        for (let i = y1; i < y2; i++)
            new_matrix.push(matrix[x1][i]);
        for (let i = x1; i < x2; i++)
            new_matrix.push(matrix[i][y2]);
        for (let i = y2; i > y1; i--)
            new_matrix.push(matrix[x2][i]);
        for (let i = x2; i > x1; i--)
            new_matrix.push(matrix[i][y1]);
        
        // 숫자를 한 칸씩 옮겨주고 최솟값 구하기
        new_matrix.unshift(new_matrix.pop());
        result.push(Math.min(...new_matrix));
        
        // 다시 new_matrix 배열에 숫자를 넣어주기
        for (let i = y1; i < y2; i++)
            matrix[x1][i] = new_matrix.shift();
        for (let i = x1; i < x2; i++)
            matrix[i][y2] = new_matrix.shift();
        for (let i = y2; i > y1; i--)
            matrix[x2][i] = new_matrix.shift();
        for (let i = x2; i > x1; i--)
            matrix[i][y1] = new_matrix.shift();
    }
    
    return result;
}