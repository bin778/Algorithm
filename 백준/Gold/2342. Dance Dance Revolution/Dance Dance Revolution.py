import sys
input = sys.stdin.readline
MAX = float('inf')

move = list(map(int, input().split()))
N = len(move)
power = [[0, 2, 2, 2, 2], [0, 1, 3, 4, 3], [0, 3, 1, 3, 4], [0, 4, 3, 1, 3], [0, 3, 4, 3, 1]]
DP = [[[MAX for _ in range(5)] for _ in range(5)] for _ in range(N)]

firstStep = move[0]
DP[0][firstStep][0] = 2
DP[0][0][firstStep] = 2

for i in range(1, N):
  step = move[i]
  for l in range(5):
    for r in range(5):
      if r != step: DP[i][step][r] = min(DP[i][step][r], DP[i-1][l][r]+power[l][step])
      if l != step: DP[i][l][step] = min(DP[i][l][step], DP[i-1][l][r]+power[r][step])
  
idx = N - 1
result = float('inf')
for i in range(5):
  for j in range(5):
    result = min(result, DP[idx][i][j])
print(result)