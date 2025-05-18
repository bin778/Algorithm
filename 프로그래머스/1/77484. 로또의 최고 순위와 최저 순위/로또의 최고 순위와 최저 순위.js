function solution(lottos, win_nums) {
    let zero = 0;
    let lotto_min = 1;
    let lotto_max = 1;
     
    // 로또 순위를 판별한다.
    for (let i = 0; i < lottos.length; i++) {
        if (!win_nums.includes(lottos[i]))
            lotto_min++;
    }
    
    for (let i = 0; i < lottos.length; i++) {
        if (lottos[i] === 0) zero++;
    }
    
    if (lotto_min === 7) lotto_min--;
    if (lotto_min - zero > 0) lotto_max = lotto_min - zero;
    
    return [lotto_max, lotto_min];
}