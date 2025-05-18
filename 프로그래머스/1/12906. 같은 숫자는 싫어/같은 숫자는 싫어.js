function solution(arr) {
    let result = [arr[0]];
    
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] !== arr[i - 1]) {
            arr[i - 1] = arr[i];
            result.push(arr[i - 1]);
        }
    }
    return result;
}