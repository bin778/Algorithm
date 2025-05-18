N, M = map(int, input().split())

board = [list(map(int, input())) for _ in range(N)]

x, y = len(board), len(board[0])
dp = [[0] * (y + 1) for _ in range(x + 1)]
result = 0
    
for i in range(1, x + 1):
  for j in range(1, y + 1):
    if board[i - 1][j - 1] == 1:
      dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    result = max(result, dp[i][j])
    
print(result * result)