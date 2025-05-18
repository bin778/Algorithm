zero = 0;
one = 0;
function quadtree(arr) {
    // 2차원 배열을 1차원으로 변환
    const arr2 = arr.reduce(function (arr, cur) {
       return arr.concat(cur); 
    });
    
    // 모든 배열이 0일 때
    if (arr2.every(x => x === 0)) {
        zero += 1;
        return;
    // 모든 배열이 1일 때
    } else if (arr2.every(x => x === 1)) {
        one += 1;
        return;
    } else {
        // 배열의 크기 계산
        const n = arr.length;
        const mid = Math.floor(n / 2);
        
        // 4개의 부분으로 나눈 배열을 저장할 변수들을 초기화
        const topLeft = [];
        const topRight = [];
        const bottomLeft = [];
        const bottomRight = [];
        
        // 배열의 4등분해서 새로운 배열에 추가하기
        for (let i = 0; i < mid; i++) {
            topLeft.push(arr[i].slice(0, mid));
            topRight.push(arr[i].slice(mid, n));
        }
        
        for (let i = mid; i < n; i++) {
            bottomLeft.push(arr[i].slice(0, mid));
            bottomRight.push(arr[i].slice(mid, n));
        }
        
        // 4등분한 배열을 재귀함수해서 모든 요소가 0 or 1인지 검사하기 
        quadtree(topLeft);
        quadtree(topRight);
        quadtree(bottomLeft);
        quadtree(bottomRight);
    }
}

function solution(arr) {
    quadtree(arr);
    return [zero, one];
}