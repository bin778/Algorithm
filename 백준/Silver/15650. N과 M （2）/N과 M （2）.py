import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * M
visited = [False for _ in range(N + 1)]

def dfs(K, num):
    if K == M:
        print(' '.join(map(str, arr)))
        return
  
    for i in range(num, N + 1):
        if visited[i]:
            continue
        
        arr[K] = i
        visited[i] = True
        dfs(K + 1, i)
        visited[i] = False

dfs(0, 1)