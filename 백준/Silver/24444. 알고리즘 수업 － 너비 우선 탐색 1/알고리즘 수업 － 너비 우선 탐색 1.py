from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1

for _ in range(M):
  U, V = map(int, input().split())
  graph[U].append(V)
  graph[V].append(U)

def bfs(node, cnt):
  queue = deque([node])
  visited[node] = 1

  while queue:
    v = queue.popleft()
    graph[v].sort()
    for i in graph[v]:
      if not visited[i]:
        cnt += 1
        queue.append(i)
        visited[i] = cnt
        queue.append(i)

bfs(R, cnt)
print(*visited[1:], sep="\n")