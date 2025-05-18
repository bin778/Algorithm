from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
lis = [A[0]]

for i in range(1, N):
  target = A[i]
  if lis[-1] < target:
    lis.append(target)
  else:
    idx = bisect_left(lis, target)
    lis[idx] = target

print(len(lis))