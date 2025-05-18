import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

indeg = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for i in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  indeg[B] += 1

def topology_sort():
  result = []
  queue = deque()

  for i in range(1, N + 1):
    if indeg[i] == 0:
      queue.append(i)
    
  while queue:
    cur = queue.popleft()
    result.append(cur)

    for i in graph[cur]:
      indeg[i] -= 1
      if indeg[i] == 0:
        queue.append(i)
  
  print(*result)

topology_sort()