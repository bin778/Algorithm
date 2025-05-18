function solution(n, works) {
    if (works.reduce((acc, curr) => acc + curr, 0) <= n) return 0;
    works.sort((a, b) => (b - a));
    
    while (n) {
        const max = works[0];
        for (let i in works) {
            if (max <= works[i]) {
                works[i] -= 1;
                n -= 1;
            }
            if (!n) break;
        }
    }
    return works.map(i => i ** 2).reduce((acc, curr) => acc + curr, 0);
}