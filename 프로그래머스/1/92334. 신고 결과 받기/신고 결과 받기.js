function solution(id_list, report, k) {
    // 신고한 내역과 신고받은 횟수 hashMap 생성, result를 0 배열로 초기화
    let hashRep = {};
    let hashSingo = {};
    const result = new Array(id_list.length).fill(0);

    id_list.map((list) => {
        hashRep[list] = new Set();
        hashSingo[list] = 0;
    });

    // 중복 제거
    const set = new Set(report);
    const uniqueArr = [...set];

    // 신고한 내역, 신고받은 횟수 hashMap 저장하기
    uniqueArr.map((singo) => {
        const user = singo.split(" ");
        if (!hashRep[user[0]].has(user[1])) {
            hashRep[user[0]].add(user[1]);
            hashSingo[user[1]]++;
        }
    });
    
    id_list.map((list, i) => {
        let n = hashRep[list];
        for (let j of n) {
            if (hashSingo[j] >= k) result[i]++;
        }
    });
    
    return result;
}