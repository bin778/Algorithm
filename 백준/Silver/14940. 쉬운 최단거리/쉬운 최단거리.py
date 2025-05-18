import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]  # 방문 여부를 기록하며, 거리를 -1로 초기화

def bfs(start_x, start_y):
  queue = deque()
  queue.append((start_x, start_y))
  visited[start_x][start_y] = 0  # 목표 지점에서의 거리는 0

  # 방향 벡터: 아래, 위, 오른쪽, 왼쪽
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  while queue:
    x, y = queue.popleft()

    for dx, dy in directions:
      nx, ny = x + dx, y + dy

      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
        if graph[nx][ny] == 1:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))
        elif graph[nx][ny] == 2:
          visited[nx][ny] = 0  # 목표 지점에서는 거리를 0으로 설정

# 목표 지점(2) 찾기
for i in range(N):
  for j in range(M):
    if graph[i][j] == 2:
      bfs(i, j)
      break

# 각 위치에서 목표 지점(2)까지의 거리 찾기
for i in range(N):
  for j in range(M):
    # graph가 0인 곳은 갈 수 없는 땅이므로 0을 출력
    if graph[i][j] == 0:
      print(0, end=' ')
    else:
      print(visited[i][j], end=' ')
  print()