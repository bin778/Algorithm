import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 배열 값 넣고 오름차순 정렬
A = [int(input()) for _ in range(N)]
A.sort()

L, R = 0, 0
result = float('inf')

while R < N:
  if A[R] - A[L] < M:
    R += 1
  else:
    result = min(result, A[R] - A[L])
    L += 1
    if L > R:
      R = L

print(result)