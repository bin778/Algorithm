function solution(numbers, hand) {
    // 배열 키패드
    // const keypad = 
    //       [[1, 2, 3],
    //        [4, 5, 6],
    //        [7, 8, 9],
    //        ["*", 0, "#"]];
    
    // 손가락 위치 인덱스 및 결과값
    let left_hand_x = 3;
    let left_hand_y = 0;
    let right_hand_x = 3;
    let right_hand_y = 2;
    let result = "";
    
    for (let i = 0; i < numbers.length; i++) {
        // 키패드가 1 or 4 or 7인 경우(왼손 엄지손가락)
        if (numbers[i] % 3 === 1) {
            left_hand_y = 0;
            result += "L";
            if (numbers[i] === 1)
                left_hand_x = 0;
            else if (numbers[i] === 4)
                left_hand_x = 1;
            else if (numbers[i] === 7)
                left_hand_x = 2;
        // 키패드가 3 or 6 or 9인 경우(오른손 엄지손가락)
        } else if (numbers[i] % 3 === 0 && numbers[i] !== 0) {
            right_hand_y = 2;
            result += "R";
            if (numbers[i] === 3)
                right_hand_x = 0;
            else if (numbers[i] === 6)
                right_hand_x = 1;
            else if (numbers[i] === 9)
                right_hand_x = 2;
        // 키패드가 2 or 5 or 6 or 0인 경우
        } else {
            let idx = -1;
            if (numbers[i] === 2)
                idx = 0;
            else if (numbers[i] === 5)
                idx = 1;
            else if (numbers[i] === 8)
                idx = 2;
            else if (numbers[i] === 0)
                idx = 3;
            
            // 왼손 거리와 오른손 거리 구하기
            const left_vector = Math.abs(idx - left_hand_x) + Math.abs(1 - left_hand_y);
            const right_vector = Math.abs(idx - right_hand_x) + Math.abs(1 - right_hand_y);
            if ((left_vector < right_vector) || ((left_vector === right_vector) && (hand === "left"))) {
                result += "L";
                left_hand_x = idx;
                left_hand_y = 1;
            } else if ((left_vector > right_vector) || ((left_vector === right_vector) && (hand === "right"))) {
                result += "R";
                right_hand_x = idx;
                right_hand_y = 1;
            }
        }
    }
    return result;
}