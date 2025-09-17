import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

test_case = int(input())

for _ in range(test_case):
  M, N, K = map(int, input().split())
  result = 0

  bachu = [[0] * M for _ in range(N)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  for i in range(K):
    A, B = map(int, input().split())
    bachu[B][A] = 1

  def dfs(x, y):
    if bachu[x][y] == 1:
      bachu[x][y] = 0

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
          continue
        elif bachu[nx][ny] == 0:
          continue
        else:
          dfs(nx, ny)
      return True
    else:
      return False

  for i in range(M):
    for j in range(N):
      if dfs(j, i): result += 1
  print(result)