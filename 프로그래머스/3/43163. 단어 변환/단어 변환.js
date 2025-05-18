function canTransform(word1, word2) {
    let diffCount = 0;
    for (let i = 0; i < word1.length; i++) {
        if (word1[i] !== word2[i]) diffCount++;
        if (diffCount > 1) return false;
    }
    return true;
}

// 두 단어가 정확히 한 문자씩 다른 지 확인
function solution(begin, target, words) {
    if (!words.includes(target)) return 0;
    
    const queue = [[begin, 0]];
    const visited = new Set();
    visited.add(begin);
    
    while (queue.length > 0) {
        const [currentWord, count] = queue.shift();
        
        // 현재 단어가 target 단어와 같으면 횟수 반환
        if (currentWord === target) return count;
        
        // 각 단어의 목록을 확인
        for (const word of words) {
            // 단어를 방문하지 않고 정확히 한 단어가 방문하면
            if (!visited.has(word) && canTransform(currentWord, word)) {
                queue.push([word, count + 1]);
                visited.add(word);
            }
        }
    }
    return 0;
}