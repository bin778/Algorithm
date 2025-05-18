function solution(files) {
    return files.sort((prev, cur) => {
        const regexHead = /\D+/; // 문자열 중에 문자인 것만 추출한다.
        const regexNumber = /\d{1,}/; // 문자열 중에 숫자인 것만 추출한다.
        const prevHead = prev.match(regexHead)[0];
        const prevNumber = prev.match(regexNumber)[0];
        const curHead = cur.match(regexHead)[0];
        const curNumber = cur.match(regexNumber)[0];
        const strCompared = prevHead.toLowerCase().localeCompare(curHead.toLowerCase());
        
        if (strCompared) return strCompared;
        return prevNumber - curNumber;
    });
}