function solution(msg) {
    const result = [];
    const dic = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    
    let i = 0;
    while (i < msg.length) {
        let j = i + 1;
        while (true) {
            // 사전에 있는 경우
            if (dic.includes(msg.slice(i, j))) {
                // 마지막 글자인 경우
                if (msg[j] === undefined) {
                    const w = msg.slice(i, j);
                    result.push(dic.indexOf(w) + 1);
                    i += w.length;
                    break;
                }
                j++;
            }
            // 사전에 없는 경우
            else {
                const w = msg.slice(i, j - 1);
                const c = msg.slice(j - 1, j);
                dic.push(w + c);
                result.push(dic.indexOf(w) + 1);
                i += w.length;
                break;
            }
        }
    }
    
    return result;
}