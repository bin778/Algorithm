import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(N)]

result = 0
max_num = 0

def dfs(x, y):
    if not (0 <= x < N and 0 <= y < M and picture[x][y] == 1):
        return 0
    
    picture[x][y] = 0
    count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        count += dfs(nx, ny)
            
    return count

for i in range(N):
    for j in range(M):
        if picture[i][j] == 1:
            result += 1
            cur_num = dfs(i, j)
            max_num = max(max_num, cur_num)

print(result)
print(max_num)