import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
R_DP = [1] * (N)
L_DP = [1] * (N)
result = [0] * (N)

for i in range(N):
  for j in range(i):
    if A[j] < A[i]:
      R_DP[i] = max(R_DP[i], R_DP[j] + 1)
    if A[-(j + 1)] < A[-(i + 1)]:
      L_DP[-(i + 1)] = max(L_DP[-(i + 1)], L_DP[-(j + 1)] + 1)

for i in range(N):
  result[i] = R_DP[i] + L_DP[i] - 1

print(max(result))