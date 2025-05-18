function find(node, parentArr) {
    if (parentArr[node] !== node)
        parentArr[node] = find(parentArr[node], parentArr);
    return parentArr[node];
}

function union(node1, node2, parentArr) {
    const a = find(node1, parentArr);
    const b = find(node2, parentArr);
    
    parentArr[Math.max(a, b)] = Math.min(a, b);
}

function solution(n, wires) {
    let result = Infinity;
    
    for (let i = 0; i < wires.length; i++) {
        // 부모 노드 초기화하기
        const parentArr = Array.from({length: n + 1}, (x, i) => i);
        for (const [idx, [v1, v2]] of wires.entries()) {
            // 간선 분리하기
            if (i === idx) continue;
            union(v1, v2, parentArr);
        }
        
        const graph = parentArr.slice(1).filter(x => parentArr[1] === find(x, parentArr)).length;
        result = Math.min(result, Math.abs(2 * graph - n));
    }
    return result;
}