function solution(prices) {
    let result = [];
    for (let i = 0; i < prices.length; i++) {
        let num = 0;
        for (let j = i + 1; j < prices.length; j++) {
            num++;
            if (prices[j] < prices[i]) break;
        }
        result.push(num);
    }
    return result;
}