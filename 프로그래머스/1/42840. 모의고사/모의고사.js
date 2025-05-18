function solution(answers) {
    const one = [..."12345".repeat(answers.length).substr(0, answers.length)];
    const two = [..."21232425".repeat(answers.length).substr(0, answers.length)];
    const three = [..."3311224455".repeat(answers.length).substr(0, answers.length)];
    
    let score = [0, 0, 0];
    let result = [];
    
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] === Number(one[i])) score[0]++;
        if (answers[i] === Number(two[i])) score[1]++;
        if (answers[i] === Number(three[i])) score[2]++;
    }
    
    const max = Math.max(...score);
    
    for (let i = 0; i < score.length; i++) {
        if (max === score[i]) result.push(i + 1);
    }
    
    return result;
}