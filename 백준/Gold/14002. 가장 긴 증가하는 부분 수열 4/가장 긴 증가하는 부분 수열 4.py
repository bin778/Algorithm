import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
DP = [0] * N

for i in range(N):
  for j in range(i):
    if A[j] < A[i] and DP[i] < DP[j] + 1:
      DP[i] = DP[j]
  DP[i] += 1

print(max(DP))

result = []
K = max(DP) + 1
for i in range(-1, -N-1, -1):
  if K - 1 == DP[i]:
    K = DP[i]
    result.append(A[i])
result.reverse()
print(*result)