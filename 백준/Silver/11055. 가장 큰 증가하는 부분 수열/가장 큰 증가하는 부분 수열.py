import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
DP = [0] * (N + 1)

for i in range(1, N + 1):
  DP[i] = A[i - 1]
  for j in range(i):
    if A[j - 1] < A[i - 1] and DP[i] < DP[j] + A[i - 1]:
      DP[i] = DP[j] + A[i - 1]

print(max(DP))