import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
DP = [[[0] * 3 for _ in range(M)] for _ in range(N)]

for i in range(N):
  for j in range(M):
    for k in range(3):
      if (j == 0 and k == 0) or (j == M - 1 and k == 2):
          DP[i][j][k] = float('inf')
          continue

      if i == 0:
          DP[i][j][k] = mat[i][j]

      if k == 0:
        DP[i][j][k] = mat[i][j] + min(DP[i - 1][j - 1][1], DP[i - 1][j - 1][2])
      elif k == 1:
        DP[i][j][k] = mat[i][j] + min(DP[i - 1][j][0], DP[i - 1][j][2])
      else:
        DP[i][j][k] = mat[i][j] + min(DP[i - 1][j + 1][0], DP[i - 1][j + 1][1])

print(min(map(min, DP[-1])))