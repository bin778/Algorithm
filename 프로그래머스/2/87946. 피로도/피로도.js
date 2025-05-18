result = 0;
function dfs(k, cnt, visited, dungeons) {
    if (cnt > result) result = cnt;
    
    for (let i = 0; i < visited.length; i++) {
        if (!visited[i] && dungeons[i][0] <= k) {
            visited[i] = true;
            dfs(k - dungeons[i][1], cnt + 1, visited, dungeons);
            visited[i] = false;
        }
    }
}

function solution(k, dungeons) {    
    const visited = Array(dungeons.length).fill(false);
    dfs(k, 0, visited, dungeons);
    return result;
}