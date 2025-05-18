import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
color = [list(input().strip()) for _ in range(N)]

# 적록색약이 아닌 경우
non_rgcb = 0 
non_rgcb_color = [row[:] for row in color]

# 적록색약인 경우
rgcb = 0 
rgcb_color = [['R' if c == 'G' else c for c in row] for row in color] 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, target_color, color_arr):
  if color_arr[x][y] == 'X':
    return 0

  if color_arr[x][y] == target_color:
    color_arr[x][y] = 'X'

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        dfs(nx, ny, target_color, color_arr)
    return 1
  else:
    return 0

for i in range(N):
  for j in range(N):
    if dfs(i, j, non_rgcb_color[i][j], non_rgcb_color):
      non_rgcb += 1
    if dfs(i, j, rgcb_color[i][j], rgcb_color):
      rgcb += 1

print(non_rgcb, rgcb)