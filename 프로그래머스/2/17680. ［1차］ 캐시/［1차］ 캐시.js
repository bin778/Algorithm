function solution(cacheSize, cities) {
    const memory = [];
    // 오랫동안 사용되지 않은 페이지가 순서대로 담겨있는 리스트
    const leastUsedList = [];
    let result = 0;
    
    for (const PAGE of cities) {
        // 들어온 페이지가 사용빈도 순서로 담겨있는 리스트에 이미 페이지가 있으면
        if (leastUsedList.includes(PAGE.toLowerCase())) {
            const PAGE_INDEX = leastUsedList.indexOf(PAGE.toLowerCase());
            // 해당하는 페이지가 있는 곳을 비우고
            leastUsedList.splice(PAGE_INDEX, 1);
        }
        // 맨 뒤(가장 최신)에 넣어줌
        leastUsedList.push(PAGE.toLowerCase());
        
        // PAGE가 메모리에 이미 있으면
        if (memory.includes(PAGE.toLowerCase())) result += 1;
        // PAGE가 메모리에 없으면
        else {
            // 메모리가 꽉 찰 경우 사용빈도 순서로 맨 앞(사용빈도가 제일 적은)의 페이지를 찾아서 교체해 줌
            if (memory.length === cacheSize) {
                const LRU_PAGE = leastUsedList.shift();
                const LRU_PAGE_INDEX = memory.indexOf(LRU_PAGE);
                memory.splice(LRU_PAGE_INDEX, 1, PAGE.toLowerCase())
            } else memory.push(PAGE.toLowerCase());
            result += 5;
        }
    }
    
    return cacheSize ? result : cities.length * 5;
}