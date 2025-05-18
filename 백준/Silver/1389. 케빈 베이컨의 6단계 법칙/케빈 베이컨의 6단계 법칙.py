import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[N for _ in range(N)] for _ in range(N)]

for _ in range(M):
  v1, v2 = map(int, input().split())
  graph[v1 - 1][v2 - 1] = 1
  graph[v2 - 1][v1 - 1] = 1

for k in range(N):
  for i in range(N):
    for j in range(N):
      if i == j: graph[i][j] = 0
      else: graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = []
for i in graph:
  result.append(sum(i))
print(result.index(min(result)) + 1)