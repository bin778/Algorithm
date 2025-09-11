function solution(s) {
    let result = "";
    let count1 = 0;
    const word = s.trim().replace(/\s+/g, ' ').split(" ");
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === " ") {
            result += " ";
        }
        else {
            let newword = "";
            for (let j = 0; j < word[count1].length; j++) {
                if (j % 2 === 0) newword += word[count1][j].toUpperCase();
                else if (j % 2 === 1) newword += word[count1][j].toLowerCase();
            }
            result += newword;
            i += newword.length - 1;
            count1++;
        }
    }
        
    return result;
}