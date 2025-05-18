function solution(array, commands) {
    let result = [];
    for (let count = 0; count < commands.length; count++)
        result.push(array.slice(commands[count][0] - 1, commands[count][1]).sort((a, b) => (a - b))[commands[count][2] - 1]);
    return result;
}