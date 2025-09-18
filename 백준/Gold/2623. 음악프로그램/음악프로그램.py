import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

indeg = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  singers = list(map(int, input().split()))[1:]
  for i in range(len(singers) - 1):
    A, B = singers[i], singers[i + 1]
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
  
  if len(result) == N:
    print(*result, sep="\n")
  else:
    print(0)

topology_sort()