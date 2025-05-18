import sys
input = sys.stdin.readline

A, B = input().split()
idx = len(B) - len(A) + 1
result = 50

for i in range(idx):
  count = 0
  for j in range(len(A)):
    if A[j] != B[i + j]:
      count += 1
  result = min(result, count)

print(result)