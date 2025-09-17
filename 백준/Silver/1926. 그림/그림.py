import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
result, cnt = 0, 0
num_list = []
picture = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y):
    global cnt
    if picture[x][y] == 1:
        picture[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                dfs(nx, ny)
        cnt += 1
        return cnt
    else:
        return 0

for i in range(N):
    for j in range(M):
        if dfs(i, j): 
            result += 1
            num_list.append(cnt)
            cnt = 0

print(result)
if num_list: print(max(num_list))
else: print(0)