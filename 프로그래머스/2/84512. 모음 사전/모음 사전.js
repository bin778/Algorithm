function solution(word) {
    let result = 0;
    const gather = ["A", "E", "I", "O", "U"];
    const num = [781, 156, 31, 6, 1];
    for (let i = 0; i < word.length; i++)
        result += (1 + (gather.indexOf(word[i]) * num[i]));
    return result;
}