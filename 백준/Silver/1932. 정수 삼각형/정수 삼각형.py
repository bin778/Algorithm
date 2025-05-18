import sys
input = sys.stdin.readline

N = int(input())
triangle = []

for _ in range(N):
  triangle.append(list(map(int, input().split())))

dp = [[0] * (i + 1) for i in range(N)]
dp[0][0] = triangle[0][0]

for i in range(1, N):
  for j in range(i + 1):
    if j - 1 >= 0:
      dp[i][j] = max(dp[i][j], triangle[i][j] + dp[i - 1][j - 1])
    if j < i:
      dp[i][j] = max(dp[i][j], triangle[i][j] + dp[i - 1][j])

print(max(dp[-1]))