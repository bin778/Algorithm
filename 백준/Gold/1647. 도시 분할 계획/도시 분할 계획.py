import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
for _ in range(M):
  A, B, C = map(int, input().split())
  edges.append((A, B, C))
edges.sort(key=lambda x: x[2])

# Union-Find
parent = [i for i in range(N + 1)]

def getParent(x):
  if parent[x] == x:
    return x
  parent[x] = getParent(parent[x])
  return parent[x]

def unionParent(a, b):
  a = getParent(a)
  b = getParent(b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def sameParent(a, b):
  return getParent(a) == getParent(b)

result = 0
lastCost = 0
for a, b, cost in edges:
  if not sameParent(a, b):
    unionParent(a, b)
    result += cost
    lastCost = cost
print(result - lastCost)