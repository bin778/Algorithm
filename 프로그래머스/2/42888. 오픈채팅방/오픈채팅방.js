function solution(record) {
    const tmpMsg = [];
    const result = [];
    const hashName = {};
    let cnt = 0;
    
    record.map((message, idx) => {
        const info = message.split(" ");
        if (info[0] === "Enter") {
            hashName[info[1]] = info[2];
            tmpMsg.push("님이 들어왔습니다.");
        } else if (info[0] === "Leave") {
            tmpMsg.push("님이 나갔습니다.");
        } else if (info[0] === "Change") {
            hashName[info[1]] = info[2];
        }
    });
    
    record.map((message, idx) => {
        const info = message.split(" ");
        if (info[0] === "Enter" || info[0] === "Leave") {
            result.push(hashName[info[1]] + tmpMsg[cnt++]);
        }
    });
    
    return result;
}