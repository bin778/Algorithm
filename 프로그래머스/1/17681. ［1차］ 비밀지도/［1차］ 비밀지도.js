function solution(n, arr1, arr2) {
    let result = [];
    let binaryArr1 = [];
    let binaryArr2 = [];
    
    // 배열에 이진수 넣기
    for (let i = 0; i < arr1.length; i++) {
        binaryArr1.push(arr1[i].toString(2).padStart(n, '0'));
        binaryArr2.push(arr2[i].toString(2).padStart(n, '0'));
    }
    
    // 이진수 연산하기
    for (let i = 0; i < binaryArr1.length; i++) {
        let temp = "";
        for (let j = 0; j < binaryArr1[i].length; j++) {
            if (binaryArr1[i][j] === "1" || binaryArr2[i][j] === "1") temp += "#";
            else temp += " ";
        }
        result.push(temp);
    }
        
    return result;
}