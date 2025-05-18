import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N)]
result = 0

def find(x):
  if x != parent[x]:
    return find(parent[x])
  return x 

def union(x, y):
  x = find(x)
  y = find(y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

for i in range(1, M + 1):
  x, y = map(int, input().split())
  if find(x) == find(y):
    result = i
    break
  union(x, y)
print(result)