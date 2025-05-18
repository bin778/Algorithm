function solution(phone_book) {
    phone_book.sort();
    for (let i = 0; i < phone_book.length - 1; i++) {
        // startsWith(searchString, position) 함수: 문자열이 특정 문자로 시작하는 지 확인하는 함수(true, false)
        // searchString 문자열의 시작 지점에서 탐색할 문자열. 정규표현식 X
        // position searchString을 탐색할 위치. 기본값은 0
        if (phone_book[i + 1].startsWith(phone_book[i]))
            return false;
    }
    return true;
}