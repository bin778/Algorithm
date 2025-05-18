function solution(board, moves) {
    const basket = [];
    let result = 0;
    
    for (let i = 0; i < moves.length; i++) {
        // 인형을 바구니에 옮기기
        for (let j = 0; j < board.length; j++) {
            if (board[j][moves[i] - 1] > 0) {
                basket.push(board[j][moves[i] - 1]);
                board[j][moves[i] - 1] = 0;
                break;
            }
        }
        
        // 바구니에 인형이 2개 있는지 검사하기
        for (let j = basket.length - 1; j >= 1; j--) {
            if (basket[j] === basket[j - 1]) {
                basket.pop();
                basket.pop();
                result += 2;
            }
        }
    }
    
    return result;
}