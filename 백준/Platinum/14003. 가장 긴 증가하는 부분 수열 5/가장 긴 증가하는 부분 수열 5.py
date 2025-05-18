from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
lis, parent = [], []

for i in A:
  if not lis:
    lis.append(i)
  if lis[-1] < i:
    lis.append(i)
    parent.append((len(lis) - 1, i))
  else:
    idx = bisect_left(lis, i)
    parent.append((idx, i))
    lis[idx]=i

result = []
last_idx = len(lis) - 1
for i in range(len(parent) -1, -1, -1):
  if parent[i][0] == last_idx:
    result.append(parent[i][1])
    last_idx -= 1
print(len(result))
result.reverse()
print(*result)