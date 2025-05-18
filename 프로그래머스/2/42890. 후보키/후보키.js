function getCombination(arr, select) {
    const result = [];
    if (select === 1) return arr.map((value) => [value]);
    
    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombination(rest, select - 1);
        const attached = combinations.map((combo) => [fixed, ...combo]);
        result.push(...attached);
    });
    
    return result;
}

function isSubset(setA, setB) {
    // setA의 모든 요소가 setB에 포함되어 있는지 확인
    return [...setA].every(element => setB.includes(element));
}

function solution(relation) {
    let result = 0;
    const uniqueness = []; // 유일성 확인을 위한 배열
    const candidateKeys = []; // 후보키를 구하는 배열
    
    const columns = Array.from({ length: relation[0].length }, (_, i) => i);
    
    // 1. 유일성 구하기
    for (let i = 1; i <= relation[0].length; i++) {
        let combinations = getCombination(columns, i);
        
        for (let combo of combinations) {
            let checkSet = new Set();
            
            // 각 조합에 해당하는 튜플을 문자열로 만들어 중복 여부 확인
            for (let row = 0; row < relation.length; row++) {
                let tuple = combo.map(col => relation[row][col]).join(',');
                checkSet.add(tuple)
            }
            
            // 유일성 확인: Set 크기와 relation의 행 수와 같은 지 확인
            if (checkSet.size === relation.length) {
                uniqueness.push(combo);
            }
        }
    }
    
    // 2. 최소성 구하기
    for (let candidate of uniqueness) {
        if (!candidateKeys.some(key => isSubset(key, candidate))) {
            candidateKeys.push(candidate);
        }
    }
    
    return candidateKeys.length;
}