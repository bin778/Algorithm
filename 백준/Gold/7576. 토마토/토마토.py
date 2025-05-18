import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for i in range(N):
  for j in range(M):
    if tomato[i][j] == 1:
      queue.append((i, j))

def bfs():
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
      nx, ny = x + dx, y + dy

      if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
        tomato[nx][ny] = tomato[x][y] + 1
        queue.append((nx, ny))

bfs()

result = 0
for i in tomato:
  if 0 in i:
    print(-1)
    exit()
  else:
    if result < max(i):
      result = max(i)

print(result - 1)