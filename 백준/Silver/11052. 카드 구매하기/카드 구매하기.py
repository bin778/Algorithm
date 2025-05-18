import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
DP = [0] * (N + 1)

for i in range(1, N + 1):
  for j in range(1, i + 1):
    DP[i] = max(DP[i], P[j] + DP[i - j])

print(DP[-1])