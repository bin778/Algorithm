import sys
input = sys.stdin.readline

N = int(input())
DP = [i for i in range(N + 1)]

for i in range(1, N + 1):
  for j in range(1, i + 1):
    if j ** 2 > i: break
    DP[i] = min(DP[i], DP[i - j ** 2] + 1)

print(DP[N])