import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(n, start):
  pq = []
  heapq.heappush(pq, (0, start))
  distance = [float('inf')] * (n + 1)
  distance[start] = 0

  # 우선순위 큐가 빌 때까지 반복
  while pq:
    dist, node = heapq.heappop(pq)
        
    if distance[node] < dist:
      continue
        
    for nextNode, weight in graph[node]:
      cost = dist + weight
      if cost < distance[nextNode]:
        distance[nextNode] = cost
        heapq.heappush(pq, (cost, nextNode))
    
  return distance

result = dijkstra(V, K)
for i in range(1, V + 1):
    if result[i] == float('inf'):
        print("INF")
    else:
        print(result[i])