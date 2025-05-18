function solution(numbers) {
    numbers.sort(function(a, b) {
        let str1 = a.toString();
        let str2 = b.toString();
        
        if (str1 === str2) {
            return 0;
        }
        
        if (str1 + str2 < str2 + str1)
            return 1;
        
        return -1;
    });
    const result = numbers.toString().replaceAll(",","");
    const reg = /[1-9]/g;
    return reg.test(result) ? result : "0";
}