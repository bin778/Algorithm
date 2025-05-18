import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

def dfs(graph, v, visited, needVisit):
    visited[v] = True
    needVisit.append(v)

    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited, needVisit)
    
    return needVisit

def bfs(graph, v):
  visited = []
  needVisit = []

  needVisit.append(v)

  while needVisit:
    node = needVisit.pop(0)
    if node not in visited:
      visited.append(node)
      needVisit.extend(graph[node])
  
  return visited

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

for i in range(1, len(graph)):
  graph[i].sort()

print(*dfs(graph, V, visited, []))
print(*bfs(graph, V))